def safety_validator(state):
    violations = []

    state.safety = {
        "approved": True,
        "violations": violations
    }
    return state
