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

    # Test translation of a valid, full-length DNA sequence with stop codons
    def test_valid_sequence(self):
        dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"  # Known DNA sequence
        expected = "MAIVMGR*KGAR*"  # Expected amino acid output using standard codon table
        translator = NucleotideTranslator(dna)  # Create instance with test DNA
        result = translator.translate()  # Call the translation method
        self.assertEqual(result, expected)  # Verify the output matches expectation

    # Test that lowercase DNA input is accepted and correctly translated
    def test_lowercase_sequence(self):
        dna = "atggcc"  # Lowercase input (often seen in raw FASTQ or FASTA)
        expected = "MA"  # Expected amino acid sequence
        translator = NucleotideTranslator(dna)  # Instantiate with lowercase input
        result = translator.translate()
        self.assertEqual(result, expected)

    # Test input with invalid nucleotide characters (e.g., 'B' is not a valid base)
    def test_invalid_characters(self):
        dna = "ATGBCC"  # Invalid sequence containing 'B'
        with self.assertRaises(ValueError):  # Expect ValueError from validation
            translator = NucleotideTranslator(dna)
            translator.translate()

    # Test behavior when sequence length is not a multiple of 3
    def test_length_not_multiple_of_three(self):
        dna = "ATGGCCG"  # 7 nucleotides — not divisible by 3
        with self.assertRaises(ValueError):  # Should raise error due to codon mismatch
            translator = NucleotideTranslator(dna)
            translator.translate()

    # Test behavior for an empty DNA sequence
    def test_empty_sequence(self):
        dna = ""  # Empty input
        with self.assertRaises(ValueError):  # Should raise error during validation
            translator = NucleotideTranslator(dna)
            translator.translate()

    # Test recognition of stop codons (e.g., TAA → '*')
    def test_stop_codon(self):
        dna = "TAA"  # Stop codon
        expected = "*"  # HGVS-recommended symbol for stop
        translator = NucleotideTranslator(dna)
        result = translator.translate()
        self.assertEqual(result, expected)


# Python standard practice: This block ensures the test suite runs only when executed directly
if __name__ == "__main__":
    unittest.main()
