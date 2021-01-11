import sys

import pytest

from numeric_matrix_processor.matrix import Matrix
from numeric_matrix_processor.matrix_generators import get_identity


@pytest.mark.parametrize("value",
                         [
                             ([[1, 7, 3], [6, 6, 4], [4, 2, 1]]),
                             ([[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [-5, 4, 12.34, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]]),
                         ])
def test_matrix_inverse(value):
    """Test inverse value"""
    initial_matrix = Matrix(value)
    zero_matrix = initial_matrix.inverse() * initial_matrix - get_identity(initial_matrix.get_lines_count())

    precision = sys.float_info.epsilon * 100

    assert all([value < precision for value in zero_matrix.values])


@pytest.mark.parametrize("value",
                         [
                             ([[2, 1], [4, 2]]),
                         ])
def test_matrix_no_inverse(value):
    """Test matrix with zeroed determinants"""
    initial_matrix = Matrix(value)

    with pytest.raises(ValueError):
        initial_matrix.inverse()

