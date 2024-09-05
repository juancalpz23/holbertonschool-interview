#!/usr/bin/python3

"""
    0-lockboxes.py

    This module has a function canUnlockAll(boxes)
    that determines if all lockboxes can be opened

"""


def canUnlockAll(boxes):
    
    """
        Determines if boxes can be opened
    """
    
    n = len(boxes)
    unlocked = [False] * n  # Track the unlocked boxes
    unlocked[0] = True  # The first box is initially unlocked
    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # If the key unlocks a new box
                unlocked[key] = True
                keys.append(key)  # Add the key to explore further boxes

    return all(unlocked)  # Return True if all boxes are unlocked
