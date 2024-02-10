"""
Difficulty: Easy
Category Strings

Caesar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns 
a new string obtained by shifting every letter in the input by k positions in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words the letter z shifted by one returns the letter a.

"""

def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = ("abcdefghijklmnopqrstuvwxyz")

    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))
    return "".join(new_letters)

def get_new_letter(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    return alphabet[new_letter_code % 26]

