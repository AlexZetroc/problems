"""
Difficulty : Easy
Category : Arrays

Sorted Square Array

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array
of the same lenght with the squares of the original integers also sorted in ascending order.
"""

array = [1, 2, 3, 4, 5, 6, 7, 8]

def sortedSquaredArray(array:list) -> list:
    second_array = []

    for number in array:
        second_array.append(number*number)

    second_array.sort()
    return second_array

print(sortedSquaredArray(array))