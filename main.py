import json
from analyzer.rules import detect_anomaly
from analyzer.reasoning import generate_reason
from analyzer.actions import suggest_action
from analyzer.confidence import calculate_confidence
from analyzer.security import check_security
from analyzer.llm_reasoning import enhance_reason_with_llm
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

api_key = os.getenv("OPENAI_API_KEY")

def process_resource(resource):
    is_anomalous, anomaly_type = detect_anomaly(resource)

    base_reason = generate_reason(resource, anomaly_type)
    reason = enhance_reason_with_llm(resource, anomaly_type, base_reason)
    action = suggest_action(anomaly_type)
    confidence = calculate_confidence(resource, anomaly_type)
    security_note = check_security(resource)

    return {
        "resource_id": resource["resource_id"],
        "is_anomalous": is_anomalous,
        "anomaly_type": anomaly_type,
        "reason": reason,
        "suggested_action": action,
        "confidence": round(confidence, 2),
        "security_note": security_note
    }


def main():
    with open("data/sample_input.json") as f:
        data = json.load(f)

    results = [process_resource(r) for r in data]

    with open("outputs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("✅ Results saved to outputs/results.json")


if __name__ == "__main__":
    main()