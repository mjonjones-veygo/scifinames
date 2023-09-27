# Sci-Fi Name Generator

A random name generator that produces names aligning with common conventions for fantasy characters in sci-fi media such as Star Wars.

## Installation

`python3 -m pip install scifinames`

Or if your project is using Poetry:

`poetry add scifinames`

## Usage

The following name generating methods are provided for a variety of different sci-fi genres:

```python
import scifinames as names

names.star_wars_name()
# Example outputs: 'Admiral Bafor Kelo'

```

## Contributing

### Poetry

This package uses [Poetry](https://python-poetry.org/) for package management. After checking out the repo, use `poetry install` to install all the required dependencies. Anytime you need to add a package, use:

```
poetry add PACKAGE_NAME_HERE
```
### Commit Convention

Before you create a Pull Request, please check whether your commits comply with
the commit conventions used in this repository.

When you create a commit we kindly ask you to follow the convention `category(scope or module): message`
in your commit message while using one of the following categories:

- `fix`: changes that fix a bug (ideally you will additionally reference an issue if present). Increases the patch version.
- `feat`: all changes that introduce completely new code or new features. Increases the minor version.

**Note that a commit that causes a BREAKING CHANGE must include `BREAKING CHANGE: <your_message>` in the footer of the commit. This increases the major version.**
