# Student Score Tracker: Dictionary-Based Aggregator

A Python-based utility designed to process student performance data. This project focuses on handling complex nested data structures and ensuring computational accuracy through manual state verification.

## Technical Implementation

* **Nested State Management**: Implements a dictionary-of-dictionaries structure to group multi-subject scores by student identity.
* **Defensive Aggregation**: Utilizes `setdefault()` for safe dictionary initialization and `try/except` blocks to handle potential `ZeroDivisionError` during average calculations.
* **Data Integrity**: Processes raw student records into structured averages for both individual subjects and overall performance.

## Logic Validation: Mechanical Execution Trace

To ensure the grouping and averaging algorithms function correctly, the system state was manually mapped through every iteration. This "mechanical autopsy" confirms that the code handles memory and variable transitions exactly as intended.

![Manual Trace Table](IMG_20260314_131636.jpg)

## Execution Instructions

Ensure you are in the project root directory, then run:

```bash
python student-score-tracker/student_logic.py
