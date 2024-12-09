# Exam3- pyton 
# Diving Scoring Program

## Overview
This Python program calculates final scores for Olympic diving events based on judge scores and degrees of difficulty (DD). It reads a tab-separated input file (`input.txt`), processes the data, and outputs a formatted table with the results.

---

## Features
- **Reads Input File**: Supports tab-separated files containing diver names, degree of difficulty, and 7 judge scores.
- **Score Calculation**:
  - Removes the highest and lowest judge scores (only one instance of each).
  - Averages the remaining scores.
  - Multiplies the average by the DD to compute the final score.
- **Formatted Output**: Outputs results in a clean, readable table.

---

## Input File Requirements
The input file should:
1. Be named `input.txt`.
2. Be located in the same directory as the Python script.
3. Contain tab-separated lines in the following format:
