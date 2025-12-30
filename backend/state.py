from typing import List, Dict, Any
from pydantic import BaseModel

class IncidentState(BaseModel):
    incident_id: str
    raw_events: List[Dict[str, Any]] = []

    analysis: Dict[str, Any] = {}
    root_cause: Dict[str, Any] = {}
    fix_plan: Dict[str, Any] = {}
    safety: Dict[str, Any] = {}
    execution: Dict[str, Any] = {}
