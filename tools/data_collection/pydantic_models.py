# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0
from datetime import datetime

from pydantic import BaseModel, Field
from typing import List, Optional, Dict

"""
Definition of the pydantic models used to descibe the run of a model.
"""


class Operation(BaseModel):
    """
    Contains information about an op's schema.
    """

    op_name: str = Field("N/A", description="Name of the op. Typically aten. or ttnn.")
    op_schema: str = Field(
        "N/A",
        description="Schema information that may include type, shape, and values.",
    )


class ModelRun(BaseModel):
    """
    Contains information about the run of a model.
    """

    name: str = Field("N/A", description="Name of the model.")
    path_in_repo: str = Field("N/A", description="Link to the relative path of the model files in repo.")
    run_success: bool = Field(None, description="Success status of the run.")
    original_run_time: float = Field(None, description="Run time in ms of the original model run before conversions.")
    compile_time: float = Field(None, description="Time spent in ms compiling the model.")
    compiled_run_time: float = Field(None, description="Run time in ms of the compiled model run after conversions.")
    accuracy: float = Field(
        None,
        description="Accuracy in %% between the original and compiled model outputs.",
    )
    ops_original: List[Operation] = Field(None, description="List of Operations of original model before conversion.")
    ops_compiled: List[Operation] = Field(None, description="List of Operations of compiled model after conversion.")
    graph_before: str = Field("N/A", description="Link to the visual graph of model before conversions.")
    graph_after: str = Field("N/A", description="Link to the visual graph of model after conversions.")
    memory_footprint: str = Field("N/A", description="Link to the visual chart of memory footprint of the model.")
    fit_in_memory: str = Field(None, description="Whether model fits in SRAM.")
    peak_sram_usage: float = Field(
        None,
        description="What is the peak SRAM usage (in MB) for a model during its execution phase.",
    )
    batch_size: int = Field(1, description="Batch size of model inputs.")


class TensorDesc(BaseModel):
    """
    Contains descriptions of tensors used as inputs or outputs of the operation in a ML
    kernel operation test.
    """

    shape: List[int] = Field(description="Shape of the tensor.")
    data_type: str = Field(description="Data type of the tensor, e.g. Float32, " "BFloat16, etc.")
    buffer_type: str = Field(description="Memory space of the tensor, e.g. Dram, L1, " "System.")
    layout: str = Field(description="Layout of the tensor, e.g. Interleaved, " "SingleBank, HeightSharded.")
    grid_shape: List[int] = Field(
        description="The grid shape describes a 2D region of cores which are used to "
        "store the tensor in memory. E.g. You have a tensor with shape "
        "128x128, you might decide to put this on a 2x2 grid of cores, "
        "meaning each core has a 64x64 slice."
    )


class OpTest(BaseModel):
    """
    Contains information about ML kernel operation tests, such as test execution,
    results, configuration.
    """

    github_job_id: int = Field(
        description="Identifier for the Github Actions CI job, which ran the test.",
    )
    full_test_name: str = Field(description="Test name plus config.")
    test_start_ts: datetime = Field(description="Timestamp with timezone when the test execution started.")
    test_end_ts: datetime = Field(description="Timestamp with timezone when the test execution ended.")
    test_case_name: str = Field(description="Name of the pytest function.")
    filepath: str = Field(description="Test file path and name.")
    success: bool = Field(description="Test execution success.")
    skipped: bool = Field(description="Some tests in a job can be skipped.")
    error_message: Optional[str] = Field(None, description="Succinct error string, such as exception type.")
    config: Optional[dict] = Field(default=None, description="Test configuration, as key/value pairs.")
    frontend: str = Field(description="ML frontend or framework used to run the test.")
    model_name: str = Field(description="Name of the ML model in which this operation is used.")
    op_kind: str = Field(description="Kind of operation, e.g. Eltwise.")
    op_name: str = Field(description="Name of the operation, e.g. ttnn.conv2d")
    framework_op_name: str = Field(description="Name of the operation within the framework, e.g. torch.conv2d")
    inputs: List[TensorDesc] = Field(description="List of input tensors.")
    outputs: List[TensorDesc] = Field(description="List of output tensors.")
    op_params: Optional[dict] = Field(
        default=None,
        description="Parametrization criteria for the operation, based on its kind, "
        "as key/value pairs, e.g. stride, padding, etc.",
    )


class AtenOpInfo(BaseModel):
    """
    Contains information about a single remaining aten operation after compilation.
    """

    op_name: str = Field(description="Name of the aten operation, e.g. 'aten.add.Tensor'")
    node_name: str = Field(description="Name of the node in the graph")
    args_str: str = Field(description="String representation of the operation arguments")
    kwargs_str: str = Field(description="String representation of the operation keyword arguments")
    input_shapes: List[str] = Field(default_factory=list, description="Input tensor shapes if available from metadata")
    output_shape: Optional[str] = Field(None, description="Output tensor shape if available from metadata")


class AtenOpsSummary(BaseModel):
    """
    Contains summary information about remaining aten operations after compilation.
    """

    total_remaining_ops: int = Field(description="Total number of remaining aten operations")
    unique_op_types: int = Field(description="Number of unique aten operation types")
    op_frequency: Dict[str, int] = Field(description="Frequency count of each aten operation type")
    most_frequent_ops: List[str] = Field(description="List of most frequently occurring aten ops")
    remaining_ops_details: List[AtenOpInfo] = Field(description="Detailed information about each remaining aten op")
    original_ops_count: Optional[int] = Field(None, description="Original number of aten ops before compilation")
    conversion_percentage: Optional[float] = Field(None, description="Percentage of ops successfully converted")
    compilation_timestamp: datetime = Field(
        default_factory=datetime.now, description="When the compilation analysis was performed"
    )
