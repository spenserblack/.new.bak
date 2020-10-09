# `.new .bak`

![CI](https://github.com/spenserblack/.new.bak/workflows/CI/badge.svg)
[![Build Status](https://travis-ci.com/spenserblack/.new.bak.svg?branch=master)](https://travis-ci.com/spenserblack/.new.bak)

Finds all files in a directory with the `.new` extension, adds `.bak` to their corresponding "old"
files, then strips the `.new` extension.

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
