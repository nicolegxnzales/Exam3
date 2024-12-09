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

--
# Sample Input File Data:
Bob Smith 1 7.5 0.5 8.5 6.5 2.5 8.0 9.5
Bob Smith 5 0.5 5.5 5.5 0.5 9.5 10.0 6.5
Paul Phillips 3 2.5 2.0 8.0 9.0 4.5 7.0 5.5
Paul Phillips 1 6.0 1.5 2.5 4.0 1.0 10.0 8.5
Molly Brown 1 9.0 5.0 1.5 9.0 4.0 0.0 8.0
Molly Brown 2 4.5 4.5 0.5 3.0 1.5 0.5 1.0
--
# Sample Output Example:
Name DD Score
Bob Smith 1.0 6.6
Bob Smith 5.0 27.5
Paul Phillips 3.0 16.5
Paul Phillips 1.0 4.5
Molly Brown 1.0 5.5
Molly Brown 2.0 4.2

---

## Input File Requirements
The input file should:
1. Be named `input.txt`.
2. Be located in the same directory as the Python script.
3. Contain tab-separated lines in the following format:
