#!/usr/bin/env python3
# This shebang line ensures the script runs using the system's Python 3 interpreter.

"""
translate_v1.py
---------------
This script converts a DNA nucleotide sequence into an amino acid (protein) sequence.

- Designed using Object-Oriented Programming (OOP) principles.
- Follows SOP for software development in clinical bioinformatics context.
- Intended for command-line use, accepts input via `--seq` argument.

Author: Samson Olofinsae
Version: 1.0
Date: 2025-06-04

Usage Example:
    python3 translate_v1.py --seq ATGGCGTAA
"""

import argparse  # Standard Python module for parsing command-line arguments


class NucleotideTranslator:
    """
    A class that encapsulates the logic for validating and translating
    a DNA sequence into a protein sequence using the standard codon table.

    Key Functions:
    - __init__: Initialises with DNA input
    - validate: Ensures sequence integrity
    - translate: Converts sequence to amino acids
    """

    # Dictionary mapping each codon (3-letter DNA string) to its corresponding amino acid (1-letter symbol)
    # This is based on the standard genetic code
    CODON_TABLE = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',  # Isoleucine & Start codon (Methionine)
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',  # Threonine
        'AAC':'N', 'AAT':'N',                        # Asparagine
        'AAA':'K', 'AAG':'K',                        # Lysine
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',  # Serine & Arginine
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',  # Leucine
        'CCA':'P', #'CCC':'P', 'CCG':'P', 'CCT':'P',  # Proline
        'CAC':'H', 'CAT':'H',                        # Histidine
        'CAA':'Q', 'CAG':'Q',                        # Glutamine
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',  # Arginine
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',  # Valine
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',  # Alanine
        'GAC':'D', 'GAT':'D',                        # Aspartic acid
        'GAA':'E', 'GAG':'E',                        # Glutamic acid
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',  # Glycine
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',  # Serine
        'TTC':'F', 'TTT':'F',                        # Phenylalanine
        'TTA':'L', 'TTG':'L',                        # Leucine
        'TAC':'Y', 'TAT':'Y',                        # Tyrosine
        'TAA':'*', 'TAG':'*', 'TGA':'*',            # Stop codons (represented as '*' based on HGVS Standard)
        'TGC':'C', 'TGT':'C',                        # Cysteine
        'TGG':'W'                                    # Tryptophan
    }

    def __init__(self, sequence):
        """
        Constructor method to initialise the translator object.

        Parameters:
        sequence (str): DNA sequence input, must contain only A, T, C, G characters.
        """
        self.sequence = sequence.upper()  # Normalise input to uppercase for consistency

    def validate(self):
        
        """Check if the sequence is an empty string (i.e., no input provided)
        This prevents silent processing of empty inputs, which could cause confusion in clinical pipelines"""
        if not self.sequence:
            raise ValueError("Sequence is empty. Please provide a DNA sequence.")

        """
        Checks whether the sequence:
        - Contains only valid nucleotides (A, T, C, G)
        - Is divisible by 3 for codon integrity

        Raises:
        ValueError: If sequence fails either check.
        """
        
        # Ensure the sequence length allows full codons
        if len(self.sequence) % 3 != 0:
            raise ValueError("Sequence length must be divisible by 3.")

        # Validate that only allowed bases are present
        if any(base not in "ATCG" for base in self.sequence):
            raise ValueError("Sequence contains invalid characters (only A, T, C, G are allowed).")

    def translate(self):
        """
        Translates the DNA sequence into a protein sequence.

        First calls self.validate() to confirm input integrity.

        Returns:
        str: Amino acid sequence (1-letter codes). 'X' is used for unrecognised codons.
        """
        self.validate()  # Ensure input is clean before processing
        protein = ""

        # Loop through sequence in steps of 3 (codon = 3 nucleotides)
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3]  # Extract one codon
            protein += self.CODON_TABLE.get(codon, 'X')  # 'X' = unknown codon (safety fallback)

        return protein


import sys  # Required to explicitly control script exit codes

def main():
    """
    Main entry point for the script.

    Uses argparse to collect a DNA sequence from the command line.
    Instantiates the NucleotideTranslator class and prints the translated protein.
    On validation failure, prints an error message to stderr and exits with status code 1.
    """
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Translate nucleotide sequence to amino acids.")
    parser.add_argument('--seq', required=True, help="DNA sequence (e.g., ATGGCC...)")
    
    # Parse input arguments from command line
    args = parser.parse_args()

    # Instantiate the NucleotideTranslator with the provided sequence
    translator = NucleotideTranslator(args.seq)
    protein = translator.translate()

    # try:
    #     # Attempt to validate and translate the input DNA sequence
    #     protein = translator.translate()

    #     # Output the resulting amino acid sequence to stdout
    #     print("Protein:", protein)

    # except ValueError as e:
    #     # If validation fails, print the error message to stderr
    #     print("Error:", e, file=sys.stderr)

    #     # Exit with status code 1 to indicate an error (used by CLI tools and test suites)
    #     sys.exit(1)


# Standard Python practice: run `main()` only if this script is executed directly
# Prevents this block from running if the module is imported elsewhere
if __name__ == "__main__":
    main()
