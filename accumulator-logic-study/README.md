# Concept Study: The Accumulator Pattern
**What I am practicing:** Variable State Management & Iterative Logic

###  The Concept
An accumulator is a variable used to "collect" or "accumulate" data over time within a loop. This is the foundation of sums, products, and complex data processing.

### Mathematical Execution Trace
Before writing the code, I manually verified the state changes:
- **Loop Rule:** `y = y + 3`
- **Initial State:** `y = 0`
- **Iteration 1:** `0 + 3 = 3`
- **Iteration 2:** `3 + 3 = 6`
- **Iteration 3:** `6 + 3 = 9`

###  Proof of Work (Handwritten Logic)
I use Mechanical Execution Tracing to master the logic on paper before I touch the keyboard.
![Handwritten Logic Trace](./IMG_20260210_150851.jpg)

| Iteration | x (Condition) | y (Before) | Logic (y + 3) | y (After) |
| :--- | :--- | :--- | :--- | :--- |
| Initial | - | - | - | 0 |
| 1 | 1 < 5 (True) | 0 | 0 + 3 | 3 |
| 2 | 2 < 5 (True) | 3 | 3 + 3 | 6 |
| 3 | 3 < 5 (True) | 6 | 6 + 3 | 9 |
| 4 | 4 < 5 (True) | 9 | 9 + 3 | 12 |
