#!/usr/bin/env python
import os
import re
from argparse import ArgumentParser
from glob import glob
from logging import getLogger

logger = getLogger(__name__)

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

paths = [f"*.{args.new}"]
if args.recursive:
    paths.insert(0, "**")

files = glob(os.path.join(args.directory, *paths), recursive=args.recursive)
print("files:", files)

ORIGINAL_FILENAME_GROUP = "original_filename"

filename_re = re.compile(rf"^(?P<{ORIGINAL_FILENAME_GROUP}>.+)(?:\.new)$")

for filename in files:
    match = filename_re.match(filename)
    if not match:
        logger.warning(f'"{filename}" did not match regex')
        continue
    original_filename = match.group(ORIGINAL_FILENAME_GROUP)
    print("original filename:", original_filename)
