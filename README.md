# Nucleotide to Protein Translator (**Clinical OOP Edition**)

This Python script translates a **DNA nucleotide sequence** into its corresponding **amino acid sequence** using **object-oriented programming (OOP)** principles.

---

## **Purpose**

Developed as part of **clinical bioinformatics training**, in line with **departmental SOPs** on:

- **Software development**
- **Version control**
- **Audit traceability**
- **Best practice in script annotation and modularity**

---

## **Features**

- **Command-line input** via `--seq`
- **Sequence validation** (length & valid characters)
- **Translation** using the standard codon table
- **Modular, testable class design** for reuse in clinical pipelines
- **HGVS-compliant output** (stop codon represented as `*`)

---

## **Usage**

```bash
python3 translate_v1.py --seq ATGGCGTAA
```

---

## Testing

This project includes two layers of unit testing:

- **Internal Logic Tests** (`tests/test_translate.py`)  
  Verifies DNA validation, codon translation, error handling, and biological correctness.

- **Command-Line Interface (CLI) Tests** (`tests/test_cli.py`)  
  Simulates running the script with real input via the command line to validate user interaction and error output.

---

Run all tests with:

```bash
python3 -m unittest discover -s tests
```

Or run them individually:

```bash
python3 -m unittest tests/test_translate.py
python3 -m unittest tests/test_cli.py
```


---

## Training Context

This script was developed under departmental supervision as part of my Clinical Bioinformatics training programme. It demonstrates:

- Object-Oriented Programming (OOP) design
- Modular code structure for audit traceability
- Compliance with internal SOPs on script annotation and version control

It contributes to STP Equivalence evidence in Domains 2 (Scientific Practice) and 5 (Professional Practice).


## Future Improvements Based on Review

Following a constructive code review (June 2025), the following enhancements have been identified for future versions of the script:

- **Commenting Standards**: Reduce over-commenting; focus on explaining "why" rather than "what".
- **Configuration File**: Externalise the codon table into a config file (e.g., JSON or YAML) for easier updates and flexibility.
- **Batch Automation**: Add support for reading input sequences from a file (e.g., FASTA or plain text).
- **Exportable Output**: Write translated protein sequences to an output file (e.g., `.tsv` or `.csv`) for further use by clinical scientists.
- **Ambiguous Nucleotides**: Improve handling of ambiguous characters like "N", possibly with custom warnings or logs.
- **Failsafe Redesign**: Replace ambiguous `"X"` amino acid marker with an explicit warning or logging mechanism.
- **PEP8 Compliance**: Apply consistent formatting with a linter such as `flake8` or `black`.

These updates will be prioritised in future versions to enhance clinical robustness, usability, and maintainability.


---

