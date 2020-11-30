import pytest

from numeric_matrix_processor.matrix import Matrix

@pytest.mark.parametrize("value, lines, columns", [(1, 1, 1), ([1], 1, 1), ([1, 2], 1, 2), ([[1, 2, 3], [1, 2, 3]], 2, 3)])
def test_lines_and_columns(value, lines, columns):
    matrix = Matrix(value)
    assert lines == matrix.get_lines()
    assert columns == matrix.get_columns()

@pytest.mark.parametrize("value", ["1", ["1"], [[1, 2], [1]], [[1, 2], [1, "2"]], ])
def test_invalid_entries(value):
    with pytest.raises(ValueError):
        Matrix(value)
