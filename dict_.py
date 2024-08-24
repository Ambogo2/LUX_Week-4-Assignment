#!/usr/bin/env python3
"""module to find the key with the input value closest to the beginning of the dictionary"""

def closest_key(dict, value):
    """finds the key with the input value closest to the beginning of the list
	Args:
        dict: A dictionary where keys are associated with lists of values.
        value: The value to search for within the lists.

     Returns:
        key: The key corresponding to the list where the value appears closest 
             to the beginning. 
    """
    closest = None
    min_index = float('inf')

    for key, values in dict.items():
        if value in values:
            index = values.index(value)

            if index < min_index:
                min_index = index
                closest = key
    
    return closest
