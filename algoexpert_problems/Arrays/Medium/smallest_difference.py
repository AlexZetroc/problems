"""
Difficulty: Medium 
Category: Arrays

Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array)
whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from
the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example,
the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.
"""


def SmallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0

    smallest_difference = float("inf")
    current_difference = float("inf")

    smallest_pair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        first_number = arrayOne[idxOne]
        second_number = arrayTwo[idxTwo]

        if first_number > second_number:
            current_difference = first_number - second_number
            idxTwo += 1
        
        elif first_number < second_number:
            current_difference = second_number - first_number
            idxOne += 1

        else:
            return [first_number, second_number]
        
        if smallest_difference > current_difference:
            smallest_difference = current_difference
            smallest_pair = [first_number, second_number]
    return smallest_pair


#arrayOne = [-1, 5, 10, 20, 28, 3]
#arrayTwo = [26, 134, 135, 15, 17]

#print(SmallestDifference(arrayOne, arrayTwo))