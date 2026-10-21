import json

class FakeLLM:
    def complete_json(self, system, user, json_schema):
        return json.dumps({
            "intent": "NEW_REQUEST",
            "criteria": {"travel_types": ["bien"], "budget_level": "low", "month": 7},
            "missing": [], "clarifying_question": None,
        })