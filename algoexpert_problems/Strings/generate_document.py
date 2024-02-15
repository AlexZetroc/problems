"""
Difficulty: Easy
Category: Strings

Generate Document

You're given a string of available characters and a string representing a document that you need to generate.
Write a function that determines if you can generate the document using the available characters. If you
can generate the document, your function should return True; otherwise, it should return False.

You're only able to generate the document if the frequency of unique characters in the characters string is greater
than or equal to the frequency of unique characters in the document string. For example, if you're given
characters = "abcabc" and document "aabbccc" you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, including special characters, capital letters, 
numbers and spaces

Note: you can always generate the empty string ""
"""

def generate_document(characters, document):
    char_count = {}

    for character in characters:
        if character not in char_count:
            char_count[character] = 0
        char_count[character] += 1

    for character in document:
        if character not in char_count or char_count[character] == 0:
            return False
        char_count[character] -= 1
    
    return True
