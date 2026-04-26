def check_security(resource):
    if resource["internet_facing"] and resource["identity_attached"]:
        return "High risk: Internet-facing resource with identity attached."

    elif resource["internet_facing"]:
        return "Moderate risk: Resource is exposed to the internet."

    elif resource["identity_attached"]:
        return "Low risk: Identity attached, ensure least privilege."

    return None