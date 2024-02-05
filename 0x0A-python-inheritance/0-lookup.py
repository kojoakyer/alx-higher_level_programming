#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
        """Return a list an object's available attributes."""
    return (dir(obj))
