import unittest
from main import calculate

class TestPipeSystem(unittest.TestCase):

    def test_simple_1(self):
        # Read test file content
        test_file = "data/test_case_1.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "C")

    def test_simple_2(self):
        # Read test file content
        test_file = "data/test_case_2.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "B")

    def test_simple_3(self):
        # Read test file content
        test_file = "data/test_case_3.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "AC")

    def test_simple_4(self):
        # Read test file content
        test_file = "data/test_case_4.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "")

    def test_simple_5(self):
        # Read test file content
        test_file = "data/test_case_5.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "")

    def test_simple_6(self):
        # Read test file content
        test_file = "data/test_case_6.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "BC")

    def test_simple_7(self):
        # Read test file content
        test_file = "data/test_case_7.txt"

        # Call the function and get the actual output
        actual_output = calculate(test_file)

        # Assert the expected output
        self.assertEqual(actual_output, "C")

    # Add similar test methods for other test cases
    # ... (Test Case 2, 3, etc.)