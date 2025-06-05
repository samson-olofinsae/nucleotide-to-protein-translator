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
