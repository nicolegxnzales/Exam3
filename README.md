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

## Output Format
The program outputs the results in a table format with the following columns:
1. **Name**: Diver’s full name.
2. **DD**: Degree of difficulty.
3. **Score**: Final score, rounded to one decimal place.

### Example Output:
Name DD Score Bob Smith 1.0 6.6
Bob Smith 5.0 27.5 Paul Phillips 3.0 16.5 Paul Phillips 1.0 4.5
Molly Brown 1.0 5.5
Molly Brown 2.0 4.2


