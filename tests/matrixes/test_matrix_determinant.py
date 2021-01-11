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
        initial_matrix.get_cofactor_at(0, 0)
