import argparse
import gzip
import pickle
import tempfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict

import pysftp

from tools.data_collection.pydantic_models import TensorDesc, OpTest


class SendToDataTeam:
    def __init__(
        self,
        github_workflow_id: int,
        sftp_host: str,
        sftp_user: str,
        sftp_private_key: str,
        metrics_directory_name: str = "metrics",
    ):
        self.github_workflow_id = github_workflow_id
        self.sftp_host = sftp_host
        self.sftp_user = sftp_user
        self.sftp_private_key = sftp_private_key
        self.metrics_dir = Path(metrics_directory_name)

    def run(self):
        start = datetime.now()

        files = self.find_pickle_files(self.metrics_dir)
        pydantic_objects = self.collect_metrics(files)

        start_str = str(start).replace(" ", "_").replace(":", "")
        file_name = f"pytorch_{start_str}.json.gz"
        with tempfile.TemporaryDirectory() as d:
            file_path = Path(d) / file_name
            self.write_file(pydantic_objects, file_path)
            self.send_file(file_path)

    def send_file(self, file_path: Path):
        """
        Sends the given file to the data team sftp.
        Args:
            file_path: Path to the file to send.
        """
        with tempfile.NamedTemporaryFile() as private_key_file:
            private_key_file.write(bytes(self.sftp_private_key, "utf-8"))
            private_key_file.flush()
            with pysftp.Connection(
                host=self.sftp_host, username=self.sftp_user, private_key=private_key_file.name
            ) as sftp:
                sftp.put(str(file_path))

    @staticmethod
    def write_file(pydantic_objects: List[OpTest], file_path: Path):
        """
        Writes the given Pydantic objects to a compressed file in json format.
        Args:
            pydantic_objects: List of OpTest objects to write to the file.
            file_path: Path to the file to write to.

        """
        json_strings = [i.model_dump_json() for i in pydantic_objects]
        json_content = "[" + ", ".join(json_strings) + "]"
        json_bytes = bytes(json_content, "utf-8")
        with gzip.open(file_path, "wb+") as f:
            f.write(json_bytes)

    @staticmethod
    def find_pickle_files(metrics_path: Path):
        """
        Recursively searches for pickle files (.pkl) and returns a dictionary
        where keys are folder paths and values are lists of pickle files in those folders.

        Args:
            metrics_path (Path): The root directory to start the search from.

        Returns:
            dict: A dictionary of folder paths (str) and their corresponding pickle files (list of Path objects).
        """
        if not metrics_path.exists():
            raise Exception(f"`{metrics_path}` directory does not exist. Please run model tests first.")

        results = {}

        def _recursive_scan(directory):
            pickle_files = []
            for item in directory.iterdir():
                if item.is_file() and item.suffix == ".pickle":
                    pickle_files.append(item)
                elif item.is_dir():
                    _recursive_scan(item)
            if pickle_files:
                results[str(directory)] = pickle_files

        _recursive_scan(metrics_path)

        return results

    def collect_metrics(self, files: Dict[str, List[Path]]) -> List[OpTest]:
        """
        Collect the metrics from the given pickle files and return a list of OpTest objects.
        Args:
            files: A dictionary of folder paths and their corresponding pickle files.

        Returns: List of OpTest objects.
        """
        op_test_objects = []

        for model_metrics_dir, pickle_files in files.items():
            model_metrics_path = Path(model_metrics_dir)

            run_time_metrics_path = model_metrics_path / "original-run_time_metrics.pickle"
            run_time_metrics = pickle.loads(run_time_metrics_path.read_bytes())

            base_op_test_data = {
                "github_job_id": self.github_workflow_id,
                "full_test_name": run_time_metrics["test_name"],
                "test_start_ts": run_time_metrics["start_ts"],
                "test_end_ts": run_time_metrics["end_ts"],
                "test_case_name": run_time_metrics["test_name"],
                "filepath": run_time_metrics["test_filepath"],
                "success": run_time_metrics["success"],
                "skipped": False,
                "error_message": run_time_metrics.get("error_message"),
                "config": {},
                "frontend": "pytorch2.0_ttnn",
                "model_name": run_time_metrics.get("model_name"),
                "op_name": "",
                "op_kind": "",
                "framework_op_name": "",
                "inputs": [],
                "outputs": [],
                "op_params": {},
            }
            schema_list_path = model_metrics_path / "original-schema_list.pickle"

            if schema_list_path.is_file():
                schema_list = pickle.loads(schema_list_path.read_bytes())
                tensor_descriptions = defaultdict(list)

                for sl in schema_list:
                    opname = sl.get("opname", "")
                    tensor_infos = sl.get("tensor_infos", {})
                    for ti in tensor_infos:
                        ti.pop("name", None)
                        tensor_descriptions[opname].append(TensorDesc(**ti))

                for op_name, tensor_description_objects in tensor_descriptions.items():
                    op_test_data = base_op_test_data.copy()

                    op_test_data["op_name"] = op_name
                    op_test_data["inputs"] = tensor_description_objects
                    op_test = OpTest(**op_test_data)
                    op_test_objects.append(op_test)
            else:
                op_test_data = base_op_test_data.copy()
                op_test = OpTest(**op_test_data)
                op_test_objects.append(op_test)

        return op_test_objects


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send metrics to data team")

    parser.add_argument("--github_workflow_id", type=int, help="Github workflow id associated with the run.")
    parser.add_argument("--sftp_host", type=str, help="Sftp host.")
    parser.add_argument("--sftp_user", type=str, help="Sftp user.")
    parser.add_argument("--sftp_private_key", type=str, help="Path to private key.")

    args = parser.parse_args()

    sender = SendToDataTeam(
        github_workflow_id=args.github_workflow_id,
        sftp_host=args.sftp_host,
        sftp_user=args.sftp_user,
        sftp_private_key=args.sftp_private_key,
    )

    sender.run()
