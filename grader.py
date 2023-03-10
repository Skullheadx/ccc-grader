import os
import time
from runner import run
from capture import Capturing

PATH = "input/"
PROBLEM = input("Enter the name of the problem: ")  # i.e. S1
FILENAME = None
extension = ".py"

for root, dirs, files in os.walk(PATH):
    for file in files:
        if file[-file[::-1].index(".") - 1:] == extension:
            FILENAME = file

if FILENAME is None:
    raise FileNotFoundError

if PROBLEM[0] == "S" or PROBLEM[0] == "s":
    contest = "senior"
elif PROBLEM[0] == "J" or PROBLEM[0] == "j":
    contest = "junior"
else:
    contest = input("Please enter name of contest; 'senior' or 'junior': ")

test_input_path = os.path.join(PATH, os.path.join(contest, PROBLEM))

test_inputs = []
test_outputs = []

for root, dirs, files in os.walk(test_input_path):
    for i, file in enumerate(files):
        with open(os.path.join(root, file), "r") as f:
            # CCC test cases alternate between IN and OUT files.
            if "sample" in file:
                if i % 2 == 0:
                    test_inputs.insert(0,f.read())
                else:
                    test_outputs.insert(0,f.read())
            else:
                if i % 2 == 0:
                    test_inputs.append(f.read())
                else:
                    test_outputs.append(f.read())


total = min(len(test_inputs), len(test_outputs))  # Total number of questions
correct = 0  # how many are correct answered

print("-" * 30)
print(f"Evaluating {FILENAME}")

for i, test in enumerate(zip(test_inputs, test_outputs)):  # loop through each input and output
    test_input, test_output = test
    with Capturing() as program_output:  # Capture output from print()
        start = time.perf_counter()  # getting start time
        run(os.path.join(PATH, FILENAME), test_input)  # running the program + input
        end = time.perf_counter()  # getting end time

    program_time = max(round(end - start, 3), 1 * 10 ** -3)  # So the output doesn't say 0.0s

    program_output = "\n".join(program_output)
    if test_output[-1] == "\n":
        test_output = test_output[:-1]
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

print("-" * 30)
print(f"Tests passed: {correct}/{total}")
