from loop import *

test_input = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''
matrix = test_input.split('\n')

def test_get_possible_moves():
    input_char_for_expected_output = {
    'S': [(1, 0), (1, 1), (2, 1), (3, 0), (3, 1)],
    '.': [],
    'F': [(0, 3), (1, 2)],
    '7': [(1, 3), (2, 4)],
    'J': [(0, 2), (1, 1)],
    'L': [(1, 2), (2, 3)],
    '|': [(0, 3), (2, 3)],
    '-': [(0, 0), (0, 2)]
    }
    input_char_for_coords = {
    'S': [2, 0],
    '.': [1, 0],
    'F': [0 ,2],
    '7': [1, 4],
    'J': [1, 2],
    'L': [2, 2],
    '|': [1, 3],
    '-': [0, 1]
    }
    for input_char in input_char_for_expected_output:
        row, col = input_char_for_coords[input_char]
        possible_moves = get_possible_moves(row, col, input_char, matrix)
        assert possible_moves == input_char_for_expected_output[input_char]