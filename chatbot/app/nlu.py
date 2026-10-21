import json
from pydantic import ValidationError
from .schemas import NluRequest, NluResult
from .llm.base import LLMClient

SYSTEM = open("app/prompts/nlu.md", encoding="utf-8").read()

def understand(req: NluRequest, llm: LLMClient, retries: int = 1) -> NluResult:
    user = json.dumps(
        {"message": req.message,
         "current_criteria": req.dialogue_state.criteria.model_dump()},
        ensure_ascii=False)
    last_err = None
    for _ in range(retries + 1):
        raw = llm.complete_json(SYSTEM, user, NluResult.model_json_schema())
        try:
            return NluResult.model_validate_json(raw)
        except ValidationError as e:
            last_err = e
    raise ValueError(f"Đầu ra LLM không hợp lệ: {last_err}")