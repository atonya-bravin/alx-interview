#!/usr/bin/python3
"""
This is a module that tries to solve an interview question
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
1. Do not return anything. The matrix must be edited in-place.
2. You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    This is the method that does the rotation
    """
    list_copy = matrix
    current_index = 0
    matrix_length = len(matrix)
    rotated_list = []
    for index in range(matrix_length):
        rotated_list.append([])
    for current_index in range(matrix_length):
        for index in range(matrix_length):
            current_number = matrix[index][current_index]
            rotated_list[current_index].insert(0, current_number)
    matrix[0: matrix_length] = rotated_list[0: matrix_length]
