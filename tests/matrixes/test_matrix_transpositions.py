import pytest

from numeric_matrix_processor.matrix import Matrix


@pytest.mark.parametrize("value, expected, method",
                         [
                             ([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]],
                              [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
                              "transpose"
                              ),
                             ([[1, 1, 1, -1], [2, 2, 2, -2], [3, 3, 3, -3], [4, 4, 4, -4]],
                              [[-4, -3, -2, -1], [4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]],
                              "side_transpose"
                              ),
                             ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
                              [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]],
                              "vertical_transpose"
                              ),
                             ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
                              [[13, 14, 15, 16], [9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]],
                              "horizontal_transpose"
                              )
                         ])
def test_matrix_transpositions(value, expected, method):
    """Test transpositions operations"""
    initial_matrix = Matrix(value)
    expected_matrix = Matrix(expected)
    assert expected_matrix == getattr(initial_matrix, method)()
