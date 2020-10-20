# `.new .bak`

![CI](https://github.com/spenserblack/.new.bak/workflows/CI/badge.svg)
[![Build Status](https://travis-ci.com/spenserblack/.new.bak.svg?branch=master)](https://travis-ci.com/spenserblack/.new.bak)

Finds all files in a directory with the `.new` extension, adds `.bak` to their corresponding "old"
files, then strips the `.new` extension.

## Installation

```bash
pip install git+https://github.com/spenserblack/.new.bak.git@v1.1.0
```

## Usage

```bash
# see all CLI options
./main.py -h

# rename files and folders in directory dir
./main.py dir

# rename files and folders in directory dir recursively
./main.py -r dir
```

## Example

### Directory Before

```
filename                        updated
my-file                         2020/10/08
my-file.new                     2020/10/09
```

### Directory After

```
filename                        updated
my-file                         2020/10/09
my-file.bak                     2020/10/08
```

## Development

### Installing `pre-commit` Hooks

```bash
poetry run pre-commit install
```
