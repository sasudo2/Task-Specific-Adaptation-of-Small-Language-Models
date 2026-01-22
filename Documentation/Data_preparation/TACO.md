# TACO: Topics in Algorithmic Code Generation dataset

## Overview

TACO is a comprehensive dataset from BAAI containing diverse algorithmic coding problems. It includes problem descriptions, function signatures, constraints, test cases, and multiple solution implementations across various difficulty levels and topics (arrays, hashmaps, stacks, etc.). The dataset is sourced from competitive programming platforms and serves as a benchmark for evaluating code generation models.

## Data Cleaning Process

The TACO dataset was preprocessed for this project to create a focused evaluation set. The cleaning pipeline involved:

### Steps:
1. **Column Selection**: Removed non-essential columns including starter_code, metadata (name, source, url, date), complexity annotations (Expected Time/Auxiliary Space, time_limit, memory_limit), and supplementary fields (skill_types, raw_tags, picture_num, input_output).

2. **Solution Filtering**: Retained only problems with at least one valid solution, ensuring all samples have correct implementations for validation.

3. **Solution Normalization**: Extracted the first solution from each problem's solution list, standardizing the dataset to a single reference solution per problem.

4. **Format Conversion**: Aggregated cleaned data across multiple parquet files into a single CSV format (`taco_cleaned.csv`) for efficient batch processing and evaluation.

### Result:
A streamlined dataset ready for fine-tuning and evaluation, containing problem descriptions, function signatures, and reference solutions without extraneous metadata.

