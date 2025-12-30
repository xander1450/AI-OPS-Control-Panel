from tools.actions import ACTIONS

def executor(state):
    logs = []
    for step in state.fix_plan.get("steps", []):
        action = ACTIONS.get(step)
        if action:
            logs.append(action())

    state.execution = {
        "status": "completed",
        "logs": logs
    }
    return state
