# 🧪 SentnelOps Internship Assignment

**AI/ML Reasoning + Anomaly Detection System**

---

## 📌 Overview

This project implements a **hybrid AI reasoning system** to analyze infrastructure-level metrics and identify anomalies, inefficiencies, and potential security risks.

Instead of relying solely on machine learning, the system focuses on:

* **Deterministic reasoning (rule-based logic)** for reliability
* **Explainable outputs** for transparency
* **Optional LLM-based enhancement** for improved human-like explanations

The goal is not just to detect anomalies, but to **explain why they occur and suggest actionable decisions**, aligning with real-world AI system design.

---

## 🧠 Problem Statement

Given infrastructure metrics such as CPU usage, memory utilization, network activity, and exposure settings, the system must:

1. Detect whether a resource is anomalous
2. Classify the anomaly type
3. Provide a clear reasoning
4. Suggest an actionable step
5. Assign a confidence score (0–1)
6. Highlight potential security concerns (optional)

---

## 🏗️ System Architecture

```
Input Data (JSON)
        ↓
Feature Analysis
        ↓
Rule-Based Anomaly Detection
        ↓
Reasoning Engine (Template-based)
        ↓
LLM Enhancement Layer (Optional)
        ↓
Action Recommendation
        ↓
Confidence Scoring
        ↓
Security Risk Analysis
        ↓
Structured JSON Output
```

---

## ⚙️ Approach

### 🔹 1. Rule-Based Anomaly Detection

A deterministic rule engine identifies anomalies using threshold-based logic:

* **Over-provisioned** → Low CPU + High memory
* **Overloaded** → High CPU / High P95 usage
* **Network-heavy** → High network utilization
* **Balanced usage** → No anomaly (normal behavior)

👉 This ensures:

* Interpretability
* Predictability
* No dependency on training data

---

### 🔹 2. Reasoning Engine

A template-based reasoning system generates explanations using actual metric values.

Example:

> “CPU utilization is consistently low (avg 2%) while memory usage is high (70%), suggesting inefficient allocation.”

👉 This ensures:

* Data-aware explanations
* Clear human understanding

---

### 🔹 3. LLM-Based Explanation Enhancement (Optional)

An LLM (via OpenAI API) is used to refine explanations:

* Improves clarity and tone
* Adds contextual richness
* Maintains concise structure

**Important Design Choice:**

> The LLM is used only for explanation enhancement — not for anomaly detection — ensuring deterministic and reliable system behavior.

Fallback mechanism:

* If API is unavailable → system uses base reasoning

---

### 🔹 4. Confidence Scoring

Confidence is calculated using heuristic scoring based on signal strength:

* Strong anomalies → higher confidence
* Balanced signals → lower confidence

This avoids unrealistic certainty and reflects real-world ambiguity.

---

### 🔹 5. Security Risk Detection

Basic rule-based security analysis:

* Internet-facing + identity → **High risk**
* Internet-facing only → **Moderate risk**
* Identity attached → **Low risk**

---

## 📁 Project Structure

```
sentnelops-assignment/
│
├── main.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── analyzer/
│   ├── rules.py
│   ├── reasoning.py
│   ├── llm_reasoning.py
│   ├── actions.py
│   ├── confidence.py
│   ├── security.py
│
├── data/
│   └── sample_input.json
│
├── outputs/
│   └── results.json
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repo_link>
cd sentnelops-assignment
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run the program

```bash
python main.py
```

---

### 5. Output

Results will be generated in:

```
outputs/results.json
```

---

## 📤 Sample Output

```json
{
  "resource_id": "i-1",
  "is_anomalous": true,
  "anomaly_type": "over_provisioned",
  "reason": "The CPU utilization is consistently low (average 2%) while memory usage is high (70%), suggesting inefficient allocation.",
  "suggested_action": "Consider downsizing the instance.",
  "confidence": 0.84,
  "security_note": "High risk: Internet-facing resource with identity attached."
}
```

---

## ⚖️ Design Tradeoffs

### ❌ Why not pure Machine Learning?

* Limited dataset
* Lack of labeled anomalies
* Reduced explainability

### ❌ Why not pure LLM?

* Non-deterministic behavior
* Hard to control consistency
* Not reliable for core decision-making

### ✅ Why Hybrid Approach?

* Rules → reliable detection
* LLM → improved explanations
* Best balance of **control + intelligence**

---

## 🧠 Handling Ambiguity

The system explicitly accounts for uncertainty:

* Introduces **balanced_usage** category
* Avoids binary decisions when signals are weak
* Uses confidence scores to reflect uncertainty

---

## 🚀 Future Improvements

* ML-based anomaly detection (Isolation Forest, etc.)
* Time-series analysis for trends
* Advanced security heuristics
* API deployment using FastAPI
* Real-time monitoring integration

---

## 🧠 Key Takeaways

This project demonstrates:

* Explainable AI system design
* Hybrid reasoning architecture
* Practical anomaly detection
* Decision-oriented AI outputs

---

## ⚡ Final Note

This system is designed not just to detect anomalies, but to:

> **Reason, explain, and recommend actions — similar to real-world AI systems used in production environments.**

---
