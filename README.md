# VCF Image Extractor

A lightweight Python script to extract images (photos) from `.vcf` (vCard) files. 
Useful for recovering photos from contacts when standard apps fail or specifically on macOS where other tools require heavy dependencies like `ggrep`.

## Features
- No external dependencies (uses standard Python libraries).
- Works on macOS, Linux, and Windows.
- Automatically handles vCard line folding.

## Usage

1. Download `vcf_extractor.py`.
2. Run it via terminal:

```bash
python3 vcf_extractor.py my_contact.vcf
