# CodeForces Dataset Preparation

## Dataset Source
The dataset is sourced from the Coding Questions and Solutions collection on Kaggle (compiled by mpwolke). It consists of a comprehensive set of programming challenges, each featuring detailed problem descriptions paired with multiple candidate solutions.

## Cleaning and Transformation

### 1. Data Selection
We filter the dataset to retain only the essential features required for fine-tuning:
- `question`: The natural language description of the programming problem.
- `solutions`: The ground truth code solutions.

### 2. Single Solution Extraction
The raw `solutions` column contains a list of multiple solutions (e.g., `["code1", "code2", ...]`). To create a consistent training target:
- We parse the stringified list using `json`.
- We extract only the **first solution** from the list.
- We convert the list format into a single raw string of code.

### 3. Data Integrity
- Rows with missing or null solutions are dropped.
- The final dataset is exported as a CSV for easy ingestion during the training phase.

## Final Schema
| Column | Description |
| :--- | :--- |
| `question` | Problem statement (Prompt) |
| `solution` | Single ground-truth code (Target) |
