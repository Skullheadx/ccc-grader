from io import StringIO
import sys

# Running the code in a separate file because there can be variable conflicts in the grader.py file (i.e. output)
def run(file_path, test_input):
    sys.stdin = StringIO(test_input)  # Enter the test input
    exec(open(file_path).read())  # Run the code
