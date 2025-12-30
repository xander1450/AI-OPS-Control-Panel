def fix_planner(state):
    steps = []

    if state.root_cause.get("final_cause") == "Vendor ABC timeout":
        steps = ["disable_vendor_ABC", "enable_fallback_vendor"]

    state.fix_plan = {
        "steps": steps,
        "risk": "LOW"
    }
    return state
