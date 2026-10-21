from typing import Protocol

class LLMClient(Protocol):
    def complete_json(self, system: str, user: str, json_schema: dict) -> str:
        """Trả về chuỗi JSON thô. Việc kiểm tra thuộc về nlu.py."""
        ...