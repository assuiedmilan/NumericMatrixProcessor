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
                             ([[17, 18]]),
                             ([[1, 2], [3, 4], [1, 2]]),
                         ])
def test_matrix_determinant_on_non_squared_matrix(value):
    """Test determinant value"""

    initial_matrix = Matrix(value)

    with pytest.raises(AttributeError):
        initial_matrix.determinant()

    with pytest.raises(AttributeError):
        list(initial_matrix.get_cofactors())

    with pytest.raises(AttributeError):
        list(initial_matrix.get_cofactors_full_decomposition())

    with pytest.raises(AttributeError):
        initial_matrix.get_cofactor_at(0, 0)


@pytest.mark.parametrize("value",
                         [
                             ([[1, 7, 7], [6, 6, 4], [4, 2, 1]]),
                             ([[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]]),
                         ])
def test_reduced_minors(value):
    """Test that minors have correct size and are in correct numbers"""
    initial_matrix = Matrix(value)
    reduced_minors = list(initial_matrix.get_cofactors_full_decomposition())

    assert factorial(initial_matrix.shape[0]) / factorial(2) == len(reduced_minors)
    assert all([(2, 2) == minor[1].shape for minor in reduced_minors])


def test_reduced_minors_values():
    """Test cofactors and minors values"""
    initial_matrix = Matrix([[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]])
    reduced_minors = list(initial_matrix.get_cofactors_full_decomposition())

    expected_values = [(0   , Matrix([[8, 7], [7, 11]]), 1),
                       (-5  , Matrix([[9, 7], [4, 11]]), 1),
                       (25  , Matrix([[9, 8], [4, 7]]) , 1),
                       (0   , Matrix([[8, 7], [7, 11]]), 1),
                       (6   , Matrix([[3, 7], [8, 11]]), 1),
                       (-30 , Matrix([[3, 8], [8, 7]]) , 1),
                       (0   , Matrix([[9, 7], [4, 11]]), 1),
                       (0   , Matrix([[3, 7], [8, 11]]), 1),
                       (20  , Matrix([[3, 9], [8, 4]]) , 1),
                       (0   , Matrix([[9, 8], [4, 7]]) , 1),
                       (0   , Matrix([[3, 8], [8, 7]]) , 1),
                       (-3  , Matrix([[3, 9], [8, 4]]) , 1),
                       (0   , Matrix([[8, 7], [7, 11]]), 1),
                       (8   , Matrix([[9, 7], [4, 11]]), 1),
                       (-40 , Matrix([[9, 8], [4, 7]]) , 1),
                       (0   , Matrix([[8, 7], [7, 11]]), 1),
                       (-12 , Matrix([[1, 7], [5, 11]]), 1),
                       (60  , Matrix([[1, 8], [5, 7]]) , 1),
                       (0   , Matrix([[9, 7], [4, 11]]), 1),
                       (0   , Matrix([[1, 7], [5, 11]]), 1),
                       (-40 , Matrix([[1, 9], [5, 4]]) , 1),
                       (0   , Matrix([[9, 8], [4, 7]]) , 1),
                       (0   , Matrix([[1, 8], [5, 7]]) , 1),
                       (6   , Matrix([[1, 9], [5, 4]]) , 1),
                       (0   , Matrix([[8, 7], [7, 11]]), 1),
                       (-12 , Matrix([[3, 7], [8, 11]]), 1),
                       (60  , Matrix([[3, 8], [8, 7]]) , 1),
                       (0   , Matrix([[8, 7], [7, 11]]), 1),
                       (15  , Matrix([[1, 7], [5, 11]]), 1),
                       (-75 , Matrix([[1, 8], [5, 7]]) , 1),
                       (0   , Matrix([[3, 7], [8, 11]]), 1),
                       (0   , Matrix([[1, 7], [5, 11]]), 1),
                       (60  , Matrix([[1, 3], [5, 8]]) , 1),
                       (0   , Matrix([[3, 8], [8, 7]]) , 1),
                       (0   , Matrix([[1, 8], [5, 7]]) , 1),
                       (-9  , Matrix([[1, 3], [5, 8]]) , 1),
                       (0   , Matrix([[9, 7], [4, 11]]), 1),
                       (0   , Matrix([[3, 7], [8, 11]]), 1),
                       (-80 , Matrix([[3, 9], [8, 4]]) , 1),
                       (0   , Matrix([[9, 7], [4, 11]]), 1),
                       (0   , Matrix([[1, 7], [5, 11]]), 1),
                       (100 , Matrix([[1, 9], [5, 4]]) , 1),
                       (0   , Matrix([[3, 7], [8, 11]]), 1),
                       (0   , Matrix([[1, 7], [5, 11]]), 1),
                       (-120, Matrix([[1, 3], [5, 8]]) , 1),
                       (0   , Matrix([[3, 9], [8, 4]]) , 1),
                       (0   , Matrix([[1, 9], [5, 4]]) , 1),
                       (0   , Matrix([[1, 3], [5, 8]]) , 1),
                       (0   , Matrix([[9, 8], [4, 7]]) , 1),
                       (0   , Matrix([[3, 8], [8, 7]]) , 1),
                       (20  , Matrix([[3, 9], [8, 4]]) , 1),
                       (0   , Matrix([[9, 8], [4, 7]]) , 1),
                       (0   , Matrix([[1, 8], [5, 7]]) , 1),
                       (-25 , Matrix([[1, 9], [5, 4]]) , 1),
                       (0   , Matrix([[3, 8], [8, 7]]) , 1),
                       (0   , Matrix([[1, 8], [5, 7]]) , 1),
                       (30  , Matrix([[1, 3], [5, 8]]) , 1),
                       (0   , Matrix([[3, 9], [8, 4]]) , 1),
                       (0   , Matrix([[1, 9], [5, 4]]) , 1),
                       (0   , Matrix([[1, 3], [5, 8]]) , 1)]

    assert expected_values == reduced_minors
