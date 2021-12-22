#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Don't edit this file.
"""

import random
import string

min_dimension = 10
max_dimension = 23
min_word_len = 9
max_testcases = 5
letter_set = string.ascii_lowercase
directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


class SearchCase:
    def __init__(self, grid, word, ans):
        self.grid = grid
        self.word = word
        self.ans = ans

    def __str__(self):
        return "{} {}\n{}\n{}".format(
            len(self.grid),
            len(self.grid[0]),
            "\n".join([" ".join(row) for row in self.grid]),
            self.word,
        )


def is_valid(pos, width, height):
    if (0 <= pos[0] < height) and (0 <= pos[1] < width):
        return True
    else:
        return False


def get_word_len(start_pos, width, height):
    result = []
    for direction in directions:
        length = 0
        pos = start_pos
        while is_valid(pos, width, height):
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            length += 1
        result.append(length)
    if random.randint(0, 1):
        # Force the diagonal
        result[::2] = [-1 for i in result[::2]]
    return directions[result.index(max(result))], max(result)


def generate_case():
    width = random.randint(min_dimension, max_dimension)
    height = random.randint(min_dimension, max_dimension)
    grid = [[random.choice(letter_set) for j in range(width)] for i in range(height)]

    word_len = 0
    # Grab a random starting position on the grid
    # Then get a random direction for the word and its corresponding length
    while word_len < min_word_len:
        start_pos = (random.randint(0, height), random.randint(0, width))
        word_dir, word_len = get_word_len(start_pos, width, height)
    # Trim the word for extra variety, then build it
    word_len = random.randint(min(min_word_len, word_len), word_len)
    search_word = "".join([random.choice(letter_set) for _ in range(word_len)])
    # Then insert
    for i in range(word_len):
        end_pos = (start_pos[0] + (word_dir[0] * i), start_pos[1] + (word_dir[1] * i))
        grid[end_pos[0]][end_pos[1]] = search_word[i]

    # FIXME: What if the randomly generated word happened to be in the grid before we inserted it?
    if random.randint(0, 1):
        ans = (start_pos, end_pos)
    else:
        ans = None
        # I think it's appropriate to subtract 1 here (I think randint is inclusive)
        replace_idx = random.randint(0, word_len - 1)
        replace_pos = (
            start_pos[0] + (word_dir[0] * replace_idx),
            start_pos[1] + (word_dir[1] * replace_idx),
        )
        # Caeser-like random shift of a single letter
        replace_offset = random.randint(1, 25)
        replace_letter_idx = (
            list(letter_set).index(grid[replace_pos[0]][replace_pos[1]])
            + replace_offset
        )
        replace_letter = letter_set[replace_letter_idx % len(letter_set)]
        grid[replace_pos[0]][replace_pos[1]] = replace_letter

    return SearchCase(grid, search_word, ans)


if __name__ == "__main__":
    num_cases = random.randint(1, max_testcases)
    with open("test_case.txt", "w") as test_input:
        with open("correct_output.txt", "w") as test_output:
            test_input.write(str(num_cases) + "\n")
            # print(num_cases)
            for i in range(num_cases):
                case = generate_case()
                test_input.write("\n" + str(case) + "\n")
                test_output.write(
                    'Searching for "{}" in matrix {} yields:\n'.format(case.word, i)
                )
                if case.ans:
                    test_output.write(
                        "Start pos: {} to End pos: {}\n\n".format(
                            case.ans[0], case.ans[1]
                        )
                    )
                else:
                    test_output.write("The pattern was not found.\n\n")
