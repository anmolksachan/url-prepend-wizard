#!/usr/bin/env python3

import argparse
import os

BANNER = """
URL Prepend Wizard 
"""

def prepend_urls(file_path, output_dir):
    with open(file_path, "r") as f:
        urls = f.read().splitlines()

    new_urls = ["https://" + url for url in urls]

    output_path = os.path.join(output_dir, os.path.basename(file_path))
    with open(output_path, "w") as f:
        f.write("\n".join(new_urls))

    print(f"Prepended 'https://' to {len(new_urls)} URLs and saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepend 'https://' to URLs in a file")
    parser.add_argument("--file", dest="file_path", required=True, help="Path to file containing URLs")
    parser.add_argument("--output-dir", dest="output_dir", default="./output", help="Output directory (default: './output')")
    args = parser.parse_args()

    print(BANNER)
    if not os.path.isfile(args.file_path):
        print(f"Error: {args.file_path} does not exist or is not a file")
    else:
        prepend_urls(args.file_path, args.output_dir)
