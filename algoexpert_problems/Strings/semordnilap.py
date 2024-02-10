"""
Difficulty: Easy
Category: string

Semordnilap

Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward
version of the other. For example the words "diaper" and "repaid" are a semordnilap pair, as the words "palindromes" and
"semordnilap".

the order of the returned pairs and the order of the strings within each pair does not matter.
"""

def semordnilap(words):
    words_dictionary = {}
    word_pairs = []

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in words_dictionary:
            word_pairs.append([word, reversed_word])
        else:
            words_dictionary[word] = 0
    return word_pairs

words = ["diaper", "abc", "test", "cba", "repaid"]

print(semordnilap(words))