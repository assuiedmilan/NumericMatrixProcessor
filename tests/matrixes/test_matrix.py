import pytest

from matrixes.conftest import matrixes
from matrixes.conftest import matrixes_columns
from matrixes.conftest import matrixes_lines
from matrixes.conftest import matrixes_shapes
from numeric_matrix_processor.matrix import Matrix

@matrixes
def test_format(value):
    """Test that returned matrix value is always a list"""
    matrix = Matrix(value)
    assert isinstance(matrix.value, list)

@matrixes_shapes
def test_lines_count(value, shape):
    """Test lines count"""
    matrix = Matrix(value)
    assert shape[0] == matrix.get_lines_count()

@matrixes_lines
def test_lines(value, lines):
    """Test that lines are correctly represented"""
    matrix = Matrix(value)
    assert (lines == matrix.get_lines()).all()

@matrixes_shapes
def test_colums_count(value, shape):
    """Test lines count"""
    matrix = Matrix(value)
    assert shape[1] == matrix.get_columns_count()

@matrixes_columns
def test_columns(value, columns):
    """Test that columns are correctly represented"""
    matrix = Matrix(value)
    assert (columns == matrix.get_columns()).all()

@pytest.mark.parametrize("value", ["1", ["1"], [[1, 2], [1]], [[1, 2], [1, "2"]], ])
def test_invalid_entries(value):
    """Test invalid entries"""
    with pytest.raises(ValueError):
        Matrix(value)
