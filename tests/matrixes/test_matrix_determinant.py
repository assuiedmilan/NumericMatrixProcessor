from math import factorial

import pytest

from numeric_matrix_processor.matrix import Matrix


@pytest.mark.parametrize("value, expected",
                         [
                             ([[17]], 17),
                             ([[-17]], -17),
                             ([[1, 2], [3, 4]], -2),
                             ([[1, 7, 7], [6, 6, 4], [4, 2, 1]], -16),
                             ([[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]], 191),
                         ])
def test_matrix_determinant(value, expected):
    """Test determinant value"""
    initial_matrix = Matrix(value)
    assert expected == initial_matrix.determinant()


@pytest.mark.parametrize("value",
                         [
                             ([[1, 7, 7], [6, 6, 4], [4, 2, 1]]),
                             ([[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]]),
                         ])
def test_reduced_minors(value):
    """Test that minors have correct size and are in correct numbers"""
    initial_matrix = Matrix(value)
    reduced_minors = list(initial_matrix.get_reduced_minors())

    assert factorial(initial_matrix.shape[0]) / factorial(2) == len(reduced_minors)
    assert all([(2, 2) == minor[1].shape for minor in reduced_minors])


def test_reduced_minors_values():
    """Test cofactors and minors values"""
    initial_matrix = Matrix([[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]])
    reduced_minors = list(initial_matrix.get_reduced_minors())

    expected_values = [(0, Matrix([[8, 7], [7, 11]])),
                       (-5, Matrix([[9, 7], [4, 11]])),
                       (25, Matrix([[9, 8], [4, 7]])),
                       (0, Matrix([[8, 7], [7, 11]])),
                       (6, Matrix([[3, 7], [8, 11]])),
                       (-30, Matrix([[3, 8], [8, 7]])),
                       (0, Matrix([[9, 7], [4, 11]])),
                       (0, Matrix([[3, 7], [8, 11]])),
                       (20, Matrix([[3, 9], [8, 4]])),
                       (0, Matrix([[9, 8], [4, 7]])),
                       (0, Matrix([[3, 8], [8, 7]])),
                       (-3, Matrix([[3, 9], [8, 4]])),
                       (0, Matrix([[8, 7], [7, 11]])),
                       (8, Matrix([[9, 7], [4, 11]])),
                       (-40, Matrix([[9, 8], [4, 7]])),
                       (0, Matrix([[8, 7], [7, 11]])),
                       (-12, Matrix([[1, 7], [5, 11]])),
                       (60, Matrix([[1, 8], [5, 7]])),
                       (0, Matrix([[9, 7], [4, 11]])),
                       (0, Matrix([[1, 7], [5, 11]])),
                       (-40, Matrix([[1, 9], [5, 4]])),
                       (0, Matrix([[9, 8], [4, 7]])),
                       (0, Matrix([[1, 8], [5, 7]])),
                       (6, Matrix([[1, 9], [5, 4]])),
                       (0, Matrix([[8, 7], [7, 11]])),
                       (-12, Matrix([[3, 7], [8, 11]])),
                       (60, Matrix([[3, 8], [8, 7]])),
                       (0, Matrix([[8, 7], [7, 11]])),
                       (15, Matrix([[1, 7], [5, 11]])),
                       (-75, Matrix([[1, 8], [5, 7]])),
                       (0, Matrix([[3, 7], [8, 11]])),
                       (0, Matrix([[1, 7], [5, 11]])),
                       (60, Matrix([[1, 3], [5, 8]])),
                       (0, Matrix([[3, 8], [8, 7]])),
                       (0, Matrix([[1, 8], [5, 7]])),
                       (-9, Matrix([[1, 3], [5, 8]])),
                       (0, Matrix([[9, 7], [4, 11]])),
                       (0, Matrix([[3, 7], [8, 11]])),
                       (-80, Matrix([[3, 9], [8, 4]])),
                       (0, Matrix([[9, 7], [4, 11]])),
                       (0, Matrix([[1, 7], [5, 11]])),
                       (100, Matrix([[1, 9], [5, 4]])),
                       (0, Matrix([[3, 7], [8, 11]])),
                       (0, Matrix([[1, 7], [5, 11]])),
                       (-120, Matrix([[1, 3], [5, 8]])),
                       (0, Matrix([[3, 9], [8, 4]])),
                       (0, Matrix([[1, 9], [5, 4]])),
                       (0, Matrix([[1, 3], [5, 8]])),
                       (0, Matrix([[9, 8], [4, 7]])),
                       (0, Matrix([[3, 8], [8, 7]])),
                       (20, Matrix([[3, 9], [8, 4]])),
                       (0, Matrix([[9, 8], [4, 7]])),
                       (0, Matrix([[1, 8], [5, 7]])),
                       (-25, Matrix([[1, 9], [5, 4]])),
                       (0, Matrix([[3, 8], [8, 7]])),
                       (0, Matrix([[1, 8], [5, 7]])),
                       (30, Matrix([[1, 3], [5, 8]])),
                       (0, Matrix([[3, 9], [8, 4]])),
                       (0, Matrix([[1, 9], [5, 4]])),
                       (0, Matrix([[1, 3], [5, 8]]))]

    assert expected_values == reduced_minors
