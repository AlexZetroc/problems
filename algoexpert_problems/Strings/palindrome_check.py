"""
Difficulty: Easy
Category: Strings

Palindrome Check:
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings
are palindromes.
"""

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False