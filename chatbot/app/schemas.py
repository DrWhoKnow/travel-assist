from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field

class Intent(str, Enum):
    NEW_REQUEST = "NEW_REQUEST"
    REFINE = "REFINE"
    CLARIFY = "CLARIFY"

class Criteria(BaseModel):
    travel_types: list[str] = []
    budget_level: Literal["low", "mid", "high"] | None = None
    budget_max_vnd: int | None = None   # chỉ điền khi người dùng nêu số cụ thể
    month: int | None = Field(default=None, ge=1, le=12)
    regions: list[str] = []
    interests: list[str] = []

class DialogueState(BaseModel):
    criteria: Criteria = Criteria()

class NluRequest(BaseModel):
    message: str
    dialogue_state: DialogueState = DialogueState()

class NluResult(BaseModel):
    intent: Intent
    criteria: Criteria
    missing: list[str] = []
    clarifying_question: str | None = None