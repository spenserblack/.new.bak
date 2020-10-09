#!/usr/bin/env python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "directory", metavar="DIR", help="the directory to search for files"
)
parser.add_argument(
    "--new",
    metavar="EXTENSION",
    default="new",
    help="The placeholder extension of the new files",
)
parser.add_argument(
    "--bak",
    "--old",
    metavar="EXTENSION",
    default="bak",
    help="The placeholder extension of the old files",
)
parser.add_argument(
    "-r", "--recursive", action="store_true", help="Run in sub-directories"
)

args = parser.parse_args()

print("directory:", args.directory)
print("new:", args.new)
print("bak:", args.bak)
print("recurse", args.recursive)
