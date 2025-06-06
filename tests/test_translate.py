#!/usr/bin/env python3
"""
test_translate.py
-----------------
Unit test script to validate the internal logic of the NucleotideTranslator class
defined in `translate_v1.py`.

Purpose:
- To test core functionality of DNA-to-protein translation using object-oriented methods.
- To ensure correct amino acid outputs for known DNA sequences.
- To verify error handling for invalid characters, empty input, and non-triplet sequences.
- Written in compliance with best practices for clinical-grade software testing, aiding
  reproducibility, traceability, and long-term maintainability.

Author: Samson Olofinsae
Created: 2025-06-05
Usage:
    python3 -m unittest tests/test_translate.py
"""



# Import Python's built-in unittest module for writing and running unit tests
import unittest

# Import the class to be tested from the main script
from translate_v1 import NucleotideTranslator


# Define a test class that inherits from unittest.TestCase
# This class contains all unit tests for the NucleotideTranslator class
class TestNucleotideTranslator(unittest.TestCase):
    
    # setUp() is called before each test method is run
    # It's commonly used to create shared objects for all tests
    def setUp(self):
        # Instantiate the NucleotideTranslator class once for reuse in each test
        self.translator = NucleotideTranslator()

    # Test translation of a valid, full-length DNA sequence with stop codons
    def test_valid_sequence(self):
        dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"  # Known DNA sequence
        expected = "MAIVMGR*KGAR*"  # Expected amino acid output using standard codon table
        result = self.translator.translate(dna)  # Translate using the class method
        self.assertEqual(result, expected)  # Verify result matches expectation

    # Test that lowercase DNA input is accepted and correctly translated
    def test_lowercase_sequence(self):
        dna = "atggcc"  # Lowercase input (often seen in raw sequence data)
        expected = "MA"  # Expected translation
        result = self.translator.translate(dna)  # Perform translation
        self.assertEqual(result, expected)  # Check output

    # Test input with invalid nucleotide characters (e.g., 'B' is not valid)
    def test_invalid_characters(self):
        # This should raise a ValueError due to invalid character 'B'
        with self.assertRaises(ValueError):
            self.translator.translate("ATGBCC")

    # Test sequence length that is not a multiple of three
    def test_length_not_multiple_of_three(self):
        # This sequence has 7 bases; translation only works on full codons (triplets)
        with self.assertRaises(ValueError):
            self.translator.translate("ATGGCCG")

    # Test behavior for an empty DNA sequence
    def test_empty_sequence(self):
        # An empty string should trigger a ValueError for invalid input
        with self.assertRaises(ValueError):
            self.translator.translate("")

    # Test recognition of stop codons (e.g., TAA translates to '*')
    def test_stop_codon(self):
        dna = "TAA"  # Stop codon
        expected = "*"  # Expected amino acid symbol for stop
        result = self.translator.translate(dna)
        self.assertEqual(result, expected)

# If this script is run directly (not imported), run all tests in this file
if __name__ == "__main__":
    unittest.main()
