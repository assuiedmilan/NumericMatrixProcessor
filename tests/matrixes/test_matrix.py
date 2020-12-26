import pytest

from matrixes.conftest import matrixes_shapes
from numeric_matrix_processor.matrix import Matrix

@matrixes_shapes
def test_lines_count(value, shape):
    """Test lines count"""
    matrix = Matrix(value)
    assert shape[0] == matrix.get_lines_count()

@matrixes_shapes
def test_colums_count(value, shape):
    """Test lines count"""
    matrix = Matrix(value)
    assert shape[1] == matrix.get_columns_count()

@pytest.mark.parametrize("value", ["1", ["1"], [[1, 2], [1]], [[1, 2], [1, "2"]], ])
def test_invalid_entries(value):
    """Test invalid entries"""
    with pytest.raises(ValueError):
        Matrix(value)
