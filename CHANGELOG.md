# Changelog

All notable changes to this project will be documented in this file, following semantic versioning principles.



## [v2.0.0] - 2025-06-04
### Changed
- Replaced stop codon character from `'_'` to `'*'` in amino acid output to comply with HGVS nomenclature standards.
- This change alters the output format, even though the functional translation logic remains unchanged.
- Rationale for version increment: In accordance with departmental SOP **“Code Review and Versioning Procedure” (Section 7.2)**, any change that **modifies the output of the software** triggers a **major version increase** to maintain traceability and uphold version-control governance standards required for clinical-facing software.


## [v1.0.2] - 2025-06-04
### Added
- Created `.gitignore` file to exclude `__pycache__/`, `*.pyc`, and `venv/` from version control.


## [v1.0.1] - 2025-06-04
### Changed
- Updated script usage from `python` to `python3` to match environment setup.
- Revised command example in `README.md` to reflect proper interpreter usage.



## [v1.0] - 2025-06-04
### Added
- Initial implementation of the DNA-to-protein translator using object-oriented programming (OOP).
- Created `translate_v1.py` to accept nucleotide sequence via command-line argument and return translated amino acid sequence.
- Defined class `NucleotideTranslator` with validation and translation methods.
- Included embedded usage instructions and metadata headers in the script.
