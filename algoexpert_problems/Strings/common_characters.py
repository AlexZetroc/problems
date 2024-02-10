"""
Difficulty: Easy
Category Strings

Common Characters

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common
to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be
in any order.
"""

def common_characters(strings):
    characters_dictionary = {}

    for word in strings:
        unique_characters = set(word)
        for char in unique_characters:
            if char not in characters_dictionary:
                characters_dictionary[char] = 0
            characters_dictionary[char] += 1

    final_characters = []

    for character, appearances in characters_dictionary.items():
        if appearances == len(strings):
            final_characters.append(character)
    return final_characters
