def generate_reason(resource, anomaly_type):
    cpu_avg = resource["cpu_avg"]
    cpu_p95 = resource["cpu_p95"]
    memory = resource["memory_avg"]
    network = resource["network_pct"]

    if anomaly_type == "over_provisioned":
        return (
            f"CPU usage is very low (avg: {cpu_avg}%) while memory usage is relatively high ({memory}%), "
            "indicating inefficient resource allocation."
        )

    elif anomaly_type == "overloaded":
        return (
            f"CPU usage is high (avg: {cpu_avg}%, p95: {cpu_p95}%), "
            "indicating the resource is under sustained heavy load."
        )

    elif anomaly_type == "network_heavy":
        return (
            f"Network usage is high ({network}%), suggesting bandwidth-intensive operations."
        )

    elif anomaly_type == "balanced_usage":
        return (
            f"CPU ({cpu_avg}%), memory ({memory}%), and network ({network}%) "
            "are within balanced ranges, indicating normal resource utilization."
        )

    return "Insufficient data to determine anomaly."