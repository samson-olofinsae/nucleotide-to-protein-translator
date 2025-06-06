#!/usr/bin/env python3
"""
test_cli.py
-----------
Unit test script to verify the command-line interface (CLI) behavior of the nucleotide-to-protein
translator tool (`translate_v1.py`).

Purpose:
- To ensure that the script behaves correctly when invoked via the terminal with `--seq` argument.
- To validate the accuracy of stdout (amino acid output) and stderr (error handling).
- To test how the script responds to valid and invalid user input via CLI.
- Designed to simulate real-world use as per clinical software development SOPs for traceability and robustness.

Author: Samson Olofinsae
Created: 2025-06-05
Usage:
    python -m unittest tests/test_cli.py
"""




# Import Python's built-in unittest module for organising and running test cases
import unittest

# Import subprocess to allow us to run the Python script as if from the command line
import subprocess

# Import sys to dynamically refer to the Python interpreter path
import sys


# Define a test class for the CLI (Command-Line Interface) of the Nucleotide Translator
# Inherits from unittest.TestCase so each method is treated as an individual test
class TestCLINucleotideTranslator(unittest.TestCase):

    # Test that a valid DNA sequence passed via CLI returns the correct amino acid sequence
    def test_valid_sequence(self):
        # Use subprocess.run() to simulate: python translate_v1.py --seq ATGGCGTAA
        result = subprocess.run(
            [sys.executable, 'translate_v1.py', '--seq', 'ATGGCGTAA'],  # command to run
            stdout=subprocess.PIPE,     # Capture standard output
            stderr=subprocess.PIPE,     # Capture standard error
            text=True                   # Decode output as text (not bytes)
        )
        self.assertEqual(result.returncode, 0)  # Expect the script to exit successfully
        self.assertIn("MA*", result.stdout)     # Expect the output to contain the correct translation

    # Test that a sequence with invalid DNA characters returns an appropriate error
    def test_invalid_characters(self):
        # Here, 'P' is an invalid character (not A, T, C, or G)
        result = subprocess.run(
            [sys.executable, 'translate_v1.py', '--seq', 'AGGGGGGGGGGGGGP'],  # includes invalid 'P'
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)  # Script should exit with error code
        self.assertIn("invalid characters", result.stderr.lower())  # Expect specific error in stderr

    # Test that a sequence whose length is not divisible by 3 returns an error
    def test_length_not_multiple_of_three(self):
        # This sequence has 15 bases (not divisible by 3) → should trigger validation error
        result = subprocess.run(
            [sys.executable, 'translate_v1.py', '--seq', 'AGGGGGGGGGGGGGG'],  # 15 bases
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)  # Should return a non-zero error code
        self.assertIn("length must be divisible by 3", result.stderr.lower())  # Expect this error message

# This ensures the test suite runs when the script is executed directly (e.g., python test_cli.py)
if __name__ == "__main__":
    unittest.main()
