# Data Integration: Mapping LeetCode Source Code to Dataset

The primary goal of this script is to bridge the gap between a directory of individual Python solution files and a central metadata DataFrame. It ensures that each problem title is correctly matched to its corresponding implementation, regardless of slight variations in naming conventions (case sensitivity, special characters, etc.).

- **Source Dataset1:** https://www.kaggle.com/datasets/theabbie/leetcode
- **Source Dataset2:** https://www.kaggle.com/datasets/gzipchrist/leetcode-problem-dataset
- **Final Dataset:** https://www.kaggle.com/datasets/pradippokhrel45/leetcode-with-desciption-and-code
---

##  Implementation Details

### 1. Text Normalization
*Example: `1. Two Sum.py` becomes `1-two-sum`*

### 2. File Loading & Mapping
The script iterates through the `CODE_DIR` and builds an in-memory dictionary (`code_map`):
- **Filtering:** Only processes files with a `.py` extension.
- **Key-Value Pair:** The normalized filename acts as the **Key**, and the full file content acts as the **Value**.

### 3. Data Merging
Using a `lambda` function on the Pandas DataFrame:
- The script looks up each problem's `title` in the `code_map`.
- If a match is found, the code content is injected into a new `code` column.



---