def detect_anomaly(resource):
    cpu_avg = resource["cpu_avg"]
    cpu_p95 = resource["cpu_p95"]
    memory = resource["memory_avg"]
    network = resource["network_pct"]

    # strong signals
    if cpu_avg < 10 and memory > 60:
        return True, "over_provisioned"

    if cpu_avg > 85 or cpu_p95 > 95:
        return True, "overloaded"

    if network > 80:
        return True, "network_heavy"

    # weak / ambiguous zone
    if 40 < cpu_avg < 60 and 40 < memory < 60:
        return False, "balanced_usage"

    return False, None