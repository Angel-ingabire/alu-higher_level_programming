#!/usr/bin/python3
"""Defines a class Mylist that inherits from list."""


class Mylist(list):
    """A subclass of list with an additional method to print the list sorted."""

    def print_sorted(self):
        """prints the list in ascending sorted order."""
        print(sorted(self))

