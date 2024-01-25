import sys
import os
import json
import csv
import math
import matplotlib.pyplot as plt

def parse_status_json_files(status_folder, prefix = "fw_"):
    stat_dict = {}
    titles = set()

    for p in os.listdir(status_folder):
        if not p.endswith(".json"):
            continue
        if not p.startswith(prefix):
            continue
        try:
            with open(os.path.join(status_folder,p)) as f:
                j = json.load(f)
                model_name = p.replace(prefix, "").replace(".json", "")
                stat_dict[model_name] = j
                op_types = set([op_info["op_type"] for op_info in j])
                titles.update(op_types)
        except:
            pass
    titles = list(sorted(titles))
    return titles, stat_dict



def generate_node_count(titles, stat_dict, node_count_csv):
    def get_op_cnt(op_type, op_infos):
        op_types = [op_info["op_type"] for op_info in op_infos]
        return op_types.count(op_type)
    rows = [["model_name"] + titles]
    for model_name in sorted(stat_dict.keys()):
        stat = stat_dict[model_name]
        row = [model_name]
        for op_type in titles:
            cnt = str(get_op_cnt(op_type, stat))
            row.append(cnt)
        rows.append(row)
    row = ["TOTAL"]
    for i in range(1,len(rows[0])):
        row.append(sum([int(rows[j][i]) for j in range(1, len(rows))]))
    rows.append(row)

    with open(node_count_csv, "w") as f:
        csv.writer(f, quotechar = '"').writerows(rows)
    print(f"{node_count_csv} generated")

def generate_total_output_size(titles, stat_dict, size_dir):
    op_sizes = {}
    def sizeof(dtype: str):
        if dtype in ["torch.bool"]:
            return 1/8
        if dtype in ["torch.float32", "torch.int32"]:
            return 4
        if dtype in ["torch.float64", "torch.int64"]:
            return 8
        print(f"{dtype} not support")
        assert(0)

    for model_name in stat_dict.keys():
        stat = stat_dict[model_name]
        for op_info in stat:
            op_type = op_info["op_type"]
            if "outputs" in op_info:
                for idx in range(len(op_info["outputs"])):
                    name = f"{op_type}_{idx}"
                    output = op_info["outputs"][idx]
                    if "shape" in output.keys() and "dtype" in output.keys():
                        size = math.prod(output["shape"]) * sizeof(output["dtype"])
                        op_sizes.setdefault(name, [])
                        op_sizes[name].append(size)

    os.makedirs(size_dir, exist_ok=True)
    for op_type in op_sizes.keys():
        f = os.path.join(size_dir, f"{op_type}.png")
        if len(op_sizes[op_type]) > 0:
            plt.title(f"{op_type}: TOTAL distribution of output size")
            plt.xlabel("output size: prod(output_shape) * dtype")
            plt.ylabel("count")
            plt.hist(op_sizes[op_type])
            plt.savefig(f)
            plt.cla()
    print(f"{size_dir} prepared")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(),"stat")
    raw = os.path.join(out,"raw")
    assert os.path.isdir(raw) and "cannot find stat/raw folder"

    def generate(prefix = "fw_"):
        titles, stat_dict = parse_status_json_files(raw, prefix)

        generate_node_count(titles, stat_dict, os.path.join(out,f"{prefix}node_count.csv"))
        generate_total_output_size(titles, stat_dict, os.path.join(out,f"{prefix}total_output_size_dist/"))

    generate("fw_")
    generate("bw_")
