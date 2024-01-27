"""
Difficulty: Medium
Category: Arrays

You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array
to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain 
the order of the other integers.

"""

def moveElementToEnd(array, toMove):
    idx = 0
    idx_counter = 0
    appearances_toMove = 0

    while idx < len(array):
        if array[idx] == toMove:
            array.pop(idx)
            appearances_toMove += 1
        elif array[idx] != toMove:
            idx += 1
        
    while idx_counter < appearances_toMove:
        array.append(toMove)
        idx_counter += 1

    return array

#array = [2,1,2,2,2,3,4,2]
#toMove = 2

#print(moveElementToEnd(array,toMove))