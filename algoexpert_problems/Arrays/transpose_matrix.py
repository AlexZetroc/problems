"""
Difficulty: Easy
Category: Arrays

You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from
top-left to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.
"""


def transpose_matrix(matrix):
    transposed_matrix = []

    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)
    return transposed_matrix

#matrix = [[1,2,3], [4,5,6], [7,8,9]]

#print(transpose_matrix(matrix))