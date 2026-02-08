#!/usr/bin/env python3

import sys
import base64
import re
import os
import argparse

def extract_image(vcf_path):
    if not os.path.exists(vcf_path):
        print(f"Error: File '{vcf_path}' not found.")
        sys.exit(1)

    try:
        with open(vcf_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        pattern = r'PHOTO.*?:([\s\S]*?)(?=\n[A-Z]|\Z)'
        match = re.search(pattern, content)

        if match:
            raw_data = match.group(1).replace('\n ', '').replace('\n', '').replace('\r', '').strip()
            
            try:
                image_data = base64.b64decode(raw_data)
            except base64.binascii.Error:
                print("Error: Could not decode base64 data. The file might be corrupted.")
                return

            output_filename = os.path.splitext(vcf_path)[0] + ".jpg"
            
            with open(output_filename, "wb") as f:
                f.write(image_data)
            
            print(f"Success! Image extracted to: {output_filename}")
        else:
            print("No photo found in this vCard file.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract JPEG images from .vcf contact files.")
    parser.add_argument("file", help="The path to the .vcf file")
    args = parser.parse_args()

    extract_image(args.file)