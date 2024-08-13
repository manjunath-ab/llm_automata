from typing import Union
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Tuple, TypedDict

class PlanExecute(TypedDict):
    input: str
    plan: List[str]
    past_steps: List[Tuple[str, int]] 
   # past_steps: Annotated[List[Tuple], operator.add]
    response: str

class Plan(BaseModel):
    """Plan to follow in future"""

    steps: List[str] = Field(
        description="different steps to follow, should be in sorted order"
    )


class Response(BaseModel):
    """Response to user."""

    response: str


class Act(BaseModel):
    """Action to perform."""

    action: Union[Response, Plan] = Field(
        description="Action to perform. If you want to respond to user, use Response. "
        "If you need to further use tools to get the answer, use Plan."
    )