#!/usr/bin/python3
"""Module defined for unlocking lockboxes"""


def canUnlockAll(boxes):
    """Determines if all locked boxes can be opened using available keys
    Args:
    boxes (list of lists) int: where each element is a list of keys contained
    in the box
    Return: bool: True if all boxes can be opened else False"""
    num_boxes = len(boxes)
    unlocked_boxes = set([0])
    keys_to_check = set(boxes[0]).difference(set([0]))
    while len(keys_to_check) > 0:
        currKey = keys_to_check.pop()
        if not currKey or currKey >= num_boxes or currKey < 0:
            continue
        if currKey not in unlocked_boxes:
            keys_to_check = keys_to_check.union(boxes[currKey])
            unlocked_boxes.add(currKey)
    return num_boxes == len(unlocked_boxes)
