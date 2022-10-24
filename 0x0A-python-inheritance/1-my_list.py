#!/usr/bin/python3
"""defines an inherited list class mylist."""

class MyList(list):
    """implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
    if issubclass(MyList, list):
        print(sorted(self))
