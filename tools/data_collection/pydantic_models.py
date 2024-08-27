from pydantic import BaseModel, Field
from typing import List

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
