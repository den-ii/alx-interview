#!/usr/bin/python3
""" 0-validae_utf8.py """


def validUTF8(data):
    """"
    Determines if the data represents a valid UTF-8 encoding.

    Args:
        data: a list of integers representing encoding

    Returns:
        True if the data is a valid UTF-8 ecoding otherwise False.
    """
    if not data:
        return False

    if data[0] & 0x80 == 0:
        return True

    if data[0] & 0xC0 == 0xC0:
        return False

    for i in range(1, len(data)):
        if data[i] & 0xC0 != 0x80:
            return False
        return True
