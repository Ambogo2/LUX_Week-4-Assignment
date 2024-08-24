#!/usr/bin/env python3
"""program to check if a string is a palindrome or not"""

def is_palindrome(text):
    """checks whether a string is a palindrome or not using a stack
       Args:
           text (str): The string to be checked for palindrome properties.
       Returns:
            bool: True if the string is a palindrome, False otherwise.
    """
    # initializing and finding the length
    stack = []
    length = len(text)

    # push first half of the string to the stack
    for i in range(length // 2):
        stack.append(text[i])

    #determine starting index of the second half
    if length % 2 == 0:
        start = length // 2
    else:
        start = length // 2 + 1

    for i in range(start, length):
        if stack.pop()  != text[i]:
            return False
        
    return True

result = is_palindrome("radar")
print (f'{result}')
