"""
(Joke) Script that resizes an image until the neural net model predicts 
something other than what it would for the full-size image
"""

import os
import argparse
from PIL import Image
from compressor import Compressor
from jpeg_compressor import JPEGCompressor
from classify_image import Evaluator

COMPRESSION_TYPES = ["resize", "jpg"]


def input_file(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)


def output_file(string):
    if os.path.isfile(string):
        raise FileExistsError(string)
    else:
        return string


def compression_type(string):
    if string in COMPRESSION_TYPES:
        return string
    else:
        raise TypeError(string)


def main():
    parser = argparse.ArgumentParser(description="Compress an Image with AI")
    parser.add_argument(
        "compression",
        metavar="compression type",
        type=compression_type,
        help=f"Valid inputs: {COMPRESSION_TYPES}",
    )
    parser.add_argument(
        "input",
        metavar="input file",
        type=input_file,
        help="Input file to compress",
    )
    parser.add_argument(
        "output",
        metavar="output file",
        type=output_file,
        help="Output file after compression",
    )

    args = parser.parse_args()

    evaluator = Evaluator()
    if args.compression == "resize":
        compressor = Compressor(evaluator)
    elif args.compression == "jpg":
        compressor = JPEGCompressor(evaluator)

    image = Image.open(args.input).convert("RGB")

    compressed_image = compressor(image)
    compressed_image.save(args.output)


if __name__ == "__main__":
    main()
