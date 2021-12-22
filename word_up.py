#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

assert (
    "linux" in sys.platform
), "This code should be run on Linux, just a reminder to follow instructions..."
from typing import List
from typing import Tuple
from typing import Any
from typing import Union
from typing import Optional

"""
Feel free to define any other helper functions you may need for this assignment.
You must define and type-hint the below functions (in a way that satisfies the unit tests).
"""


def build_matrix(height: int, width: int) -> List[List[str]]:
    my_matrix: List[List[str]] = []
    for i in range(height):
        my_matrix.append([])
        for j in range(width):
            my_matrix[i].append("")
    return my_matrix
    """
    Should build a 2D List of Lists of empty strings, i.e., ""
    Returns a List[List[str]]
    Do NOT fill your matrix here; fill it in main, or another function.
    Write your function below here.
    """
    pass


def search_direction(
    matrix: List[List[str]],
    start_position: Tuple[int, int],
    offsetx: int,
    offsety: int,
    word: str,
) -> Optional[Tuple[int, int]]:

    X = start_position[1] + offsetx * (len(word) - 1)
    Y = start_position[0] + offsety * (len(word) - 1)

    if X < 0 or X >= len(matrix[0]) or Y < 0 or Y >= len(matrix):
        return None
    else:
        for i in range(len(word)):
            if (
                matrix[start_position[0] + i * offsety][start_position[1] + i * offsetx]
            ) != word[i]:
                return None
            else:
                k = start_position[0] + i * offsety
                j = start_position[1] + i * offsetx

                continue

        return (k, j)


def matrix_search(
    matrix: List[List[str]], word: str
) -> Union[Tuple[Tuple[int, int], Tuple[int, int]], None]:

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):

            if matrix[r][c] == word[0]:
                pos_start = (r, c)
                if (pos_end := search_direction(matrix, (r, c), -1, 0, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), 1, 0, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), 0, 1, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), 0, -1, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), -1, -1, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), 1, -1, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), -1, 1, word)) :

                    return (pos_start, pos_end)

                elif (pos_end := search_direction(matrix, (r, c), 1, 1, word)) :

                    return (pos_start, pos_end)

    return None

    """
    Should search through a matrix built above to find the word (a str).
    Returns the coordinates listed [down][over] a.k.a. [row][col].
    as a tuple of tuples of ints: Tuple[Tuple[int, int], Tuple[int, int]].
    If it does not find the word, then return None.
    matrix_search should NOT build or fill the matrix.
    Write your actual AI below here.
    """
    pass


def main() -> None:

    num_search = int(input())

    for debut in range(num_search):

        empty = input()

        height, width = map(int, input().split())

        letter_grid = build_matrix(height, width)

        for r in range(height):
            row = input().split()
            for c in range(width):
                letter_grid[r][c] = row[c]

        word = str(input())

        print('Searching for "' + word + '" in matrix', debut, "yields:")

        if (final_pos := matrix_search(letter_grid, word)) :
            print(f"Start pos: {final_pos[0]} to End pos: {final_pos[1]}")
        else:
            print("The pattern was not found.")

        print()

    """
    Write or call the code to read in the game parameters: dimensions/matrix/word here
    Main should call build_matrix and matrix_search
    """
    pass


if __name__ == "__main__":
    main()
