"""
Difficulty: Easy
Category: Strings

First Non-repeating character

Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's
first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-reapeating characters, your function should return -1
"""

def first_non_repeating_character(string):
    letter_dictionary = {}

    for letter in string:
        if letter not in letter_dictionary:
            letter_dictionary[letter] = 0
        else:
            letter_dictionary[letter] += 1
        
    for idx, letter in enumerate(string):
        if letter in letter_dictionary and letter_dictionary[letter] == 0:
            return idx
    return -1

