#!/usr/bin/env python3
"""Module to generate bigrams from a given text."""
def generate_bigrams(text):
    """
    Splits the input text into words and generates bigrams, 
    which are pairs of consecutive words.

    Args:
        text (str): The input string from which bigrams will be generated.

    Returns:
        list of tuple: A list of tuples where each tuple contains two consecutive words (bigrams).
    """
    # Split the text into words
    words = text.split()
    
    # Generate the bigrams by pairing adjacent words
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    
    return bigrams
