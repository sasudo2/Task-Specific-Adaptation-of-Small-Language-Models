# Competitive Programming Dataset: Python Code Generation

This repository contains a specialized dataset derived from the **Alpaca Python 18k** collection, refined specifically for competitive programming tasks.

##  Dataset Overview
- **Source Dataset:** [iamtarun/python_code_instructions_18k_alpaca](https://huggingface.co/datasets/iamtarun/python_code_instructions_18k_alpaca)
- **Classified Raw Data:** [Alpaca Specific Competitive Datasets](https://www.kaggle.com/datasets/pradippokhrel45/alpaca-datasets-specific-competetive-datasets)
- **Final Refined Version:** [Cleaned Datasets of Alpaca](https://www.kaggle.com/datasets/pradippokhrel45/cleaned-datasets-of-alpaca)

---

##  Preparation Pipeline

The preparation process involved automated classification using a local LLM to filter for high-quality algorithmic problems.

### 1. Environment Setup
The classification script runs in a local environment using:
* **LLM Engine:** [Ollama](https://ollama.com/)
* **Model:** `qwen2.5-coder:1.5b`
* **Concurrency:** `asyncio` and `nest_asyncio` for high-throughput batching in Python environments.

### 2. Automated Classification
We utilized a **zero-shot classification** strategy with the following configuration:
- **Temperature:** `0` (Deterministic output)
- **Batch Size:** `5` (Optimized for local hardware)


---

##  Data Cleaning Methodology

To ensure the model learns robust algorithmic patterns and avoids noise, the following filtering steps were applied:

### Threshold Filtering
Any category containing **100 or fewer rows** was discarded. This prevents the model from overfitting on underrepresented topics and ensures a more balanced training distribution.

### Domain Pruning
The following categories were automatically or manually removed as they fall outside the scope of competitive programming:
* **Web Development**
* **Machine Learning**

### Manual Refinement
After automated processing, the dataset underwent a manual review to:
1. Remove misclassified entries.
2. Ensure the instructions were clear and the code was logically correct.

---

