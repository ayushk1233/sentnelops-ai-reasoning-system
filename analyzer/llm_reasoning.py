import os
from openai import OpenAI


def enhance_reason_with_llm(resource, anomaly_type, base_reason):
    print("⚡ LLM reasoning invoked...")

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ No API key found. Using base reasoning.")
        return base_reason

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an AI system analyzing infrastructure metrics.

Resource Data:
CPU Avg: {resource['cpu_avg']}%
CPU P95: {resource['cpu_p95']}%
Memory: {resource['memory_avg']}%
Network: {resource['network_pct']}%

Detected Anomaly: {anomaly_type}

Base Explanation: {base_reason}

Rewrite this explanation to be:
- clearer
- more professional
- slightly more detailed

Keep it concise (2–3 lines max).
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        print("✅ LLM enhanced reasoning applied.")
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ LLM failed: {e}")
        return base_reason