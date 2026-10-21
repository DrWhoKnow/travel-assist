from .schemas import Criteria, Intent, NluResult

def merge(current: Criteria, result: NluResult) -> Criteria:
    if result.intent == Intent.NEW_REQUEST:
        return result.criteria
    updates = result.criteria.model_dump(exclude_defaults=True)
    return Criteria(**{**current.model_dump(), **updates})