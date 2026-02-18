# Goal: Increment variable 'y' by 3 per iteration to test accumulator logic
# y = 0  # Initial State verified via manual trace (see IMG_20260210_150851.jpg)
print(f"Initial State: y = {y}")

for i in range(1, 5):  # Iterations 1 through 4
    y = y + 3          # The Accumulator Rule
    print(f"Iteration {i}: y is now {y}")

print(f"Final Accumulator Value: {y}")
