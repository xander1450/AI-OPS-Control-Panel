from fastapi import FastAPI, Body
import uuid

from graph import app as ai_graph
from state import IncidentState

api = FastAPI()

@api.post("/incident")
def create_incident(events: list = Body(...)):
    state = IncidentState(
        incident_id=str(uuid.uuid4()),
        raw_events=events
    )
    return ai_graph.invoke(state)
