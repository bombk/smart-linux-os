def decide(metrics, anomaly):
    if anomaly and metrics["cpu"] > 85:
        return "RESTART_HEAVY_PROCESS"
    if anomaly and metrics["memory"] > 90:
        return "ALERT"
    return "NONE"
