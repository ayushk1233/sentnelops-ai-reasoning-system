def calculate_confidence(resource, anomaly_type):
    cpu_avg = resource["cpu_avg"]
    cpu_p95 = resource["cpu_p95"]
    memory = resource["memory_avg"]
    network = resource["network_pct"]

    if anomaly_type == "overloaded":
        score = (cpu_avg + cpu_p95) / 200

    elif anomaly_type == "over_provisioned":
        score = ((100 - cpu_avg) + memory) / 200

    elif anomaly_type == "network_heavy":
        score = network / 100

    else:
        return 0.4  # low confidence if no anomaly

    # clamp between 0.5 and 0.95 to avoid fake certainty
    return round(min(0.95, max(0.5, score)), 2)