def suggest_action(anomaly_type):
    if anomaly_type == "over_provisioned":
        return "Consider downsizing the instance to reduce cost."

    elif anomaly_type == "overloaded":
        return "Scale up resources or distribute load."

    elif anomaly_type == "network_heavy":
        return "Optimize network usage or introduce caching/CDN."

    elif anomaly_type == "balanced_usage":
        return "Continue monitoring for any unusual trends."

    return "Further investigation required."