import os
import time
from runner import run
from capture import Capturing

code = "code/main.py"
test_inputs = []
test_outputs = []

# Getting all the test inputs and outputs
# the corresponding input and output files should be in the same order
for root, dirs, files in os.walk("tests/input"):
    for i, file in enumerate(files):
        with open(os.path.join(root, file), "r") as f:
            test_inputs.append(f.read())

for root, dirs, files in os.walk("tests/output"):
    for i, file in enumerate(files):
        with open(os.path.join(root, file), "r") as f:
            test_outputs.append(f.read())


total = min(len(test_inputs), len(test_outputs))  # Total number of questions
correct = 0  # how many are correct answered

print("-" * 30)
print(f"Evaluating {code}\n")

for i, test in enumerate(zip(test_inputs, test_outputs)):  # loop through each input and output
    test_input, test_output = test
    with Capturing() as program_output:  # Capture output from print()
        start = time.perf_counter()  # getting start time
        run(code, test_input)  # running the program + input
        end = time.perf_counter()  # getting end time

    program_time = max(round(end - start, 3), 1 * 10 ** -3)  # So the output doesn't say 0.0s

    program_output = "\n".join(program_output)
    if test_output[-1] == "\n":
        test_output = test_output[:-1] # removing trailing newlines in the test output

    # Check if the program output is correct.
    if program_output == test_output:
        print(f"{i+1}. Test Passed. {program_time}s")
        correct += 1
    else:
        print(f"{i+1}. Test Failed. {program_time}s")
        print(f"{test_input = }")
        print(f"{test_output = }")
        print(f"{program_output = }")
        print()

print(f"Tests passed: {correct}/{total}")
print("-" * 30)
