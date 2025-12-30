def root_cause_reasoner(state):
    cause = "Unknown"

    for s in state.analysis.get("signals", []):
        if "vendor_timeout" in s.get("message", ""):
            cause = "Vendor ABC timeout"

    state.root_cause = {
        "final_cause": cause,
        "confidence": 0.8
    }
    return state
