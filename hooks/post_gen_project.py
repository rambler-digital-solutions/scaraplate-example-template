"""Conditionally remove files from the generated project depending on
the cookiecutter template variables.

See https://github.com/cookiecutter/cookiecutter/issues/723
"""
import os


def main():
    if "{{ cookiecutter.mypy_enabled }}" != "1":
        os.remove("mypy.ini")


if __name__ == "__main__":
    main()
