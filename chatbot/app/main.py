from fastapi import FastAPI
from .schemas import NluRequest
from .nlu import understand
from .dialogue import merge
from .llm.fake import FakeLLM

app = FastAPI()
llm = FakeLLM()   # đổi sang client thật khi chốt nhà cung cấp

@app.post("/nlu")
def nlu(req: NluRequest):
    result = understand(req, llm)
    merged = merge(req.dialogue_state.criteria, result)
    return {**result.model_dump(), "merged_criteria": merged.model_dump()}