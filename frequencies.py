"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        str_item = str(item)
        count = 0
        for other in items:
            if str(other) == str_item:
                count += 1
        if not frequencies:
            frequencies[str_item] = count
        elif frequencies and str_item not in frequencies:
            frequencies[str_item] = count
    return frequencies
