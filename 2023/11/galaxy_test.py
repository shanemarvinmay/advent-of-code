import pytest
from galaxy import *

@pytest.fixture
def setup_m():
    m = test_input.split('\n')
    yield m

def test_get_expanse_rows_cols(setup_m):
    expected_expanse_rows = [3, 7]
    expected_expanse_cols = [2, 5, 8]
    expanse_rows, expanse_cols = get_expanse_rows_cols(setup_m)
    assert expanse_rows == expected_expanse_rows, 'Testing expanse rows.'
    assert expanse_cols == expected_expanse_cols, 'Testing expanse cols.'

def test_get_galaxy_coords(setup_m):
    expected_galaxy_coords = [[0, 3], [1, 7], [2, 0], [4, 6], [5, 1], [6, 9], [8, 7], [9, 0], [9, 4]]
    assert get_galaxy_coords(setup_m) == expected_galaxy_coords, 'Testing galaxy coords'

def test_adjust_coords_for_expanse():
    expected_galaxy_expanse_coords = [[0, 4], [1, 9], [2, 0], [5, 8], [6, 1], [7, 12], [10, 9], [11, 0], [11, 5]]
    galaxy_coords = [[0, 3], [1, 7], [2, 0], [4, 6], [5, 1], [6, 9], [8, 7], [9, 0], [9, 4]]
    expanse_rows = [3, 7]
    expanse_cols = [2, 5, 8]

    adjust_coords_for_expanse(galaxy_coords, expanse_rows, expanse_cols)

    assert galaxy_coords == expected_galaxy_expanse_coords, 'Testing galaxy expanse coords.'

def test_get_sum_of_shortest_path_for_galaxy_pairs():
    expected_total_distance = 374
    galaxy_coords = [[0, 4], [1, 9], [2, 0], [5, 8], [6, 1], [7, 12], [10, 9], [11, 0], [11, 5]]

    total_distance = get_sum_of_shortest_path_for_galaxy_pairs(galaxy_coords)

    assert total_distance == expected_total_distance, 'Testing total distance of shortest path between each pair of galaxies.'

