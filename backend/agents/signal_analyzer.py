def signal_analyzer(state):
    severity = "LOW"
    if any(e.get("error_rate", 0) > 5 for e in state.raw_events):
        severity = "HIGH"

    state.analysis = {
        "severity": severity,
        "signals": state.raw_events
    }
    return state
