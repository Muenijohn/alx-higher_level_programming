#!/usr/bin/python3
"""Defines a file-writing function."""



def read_file(filename=""):
    """print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf8") as f:
        print(f.reaad(), end="")
