from itertools import product

import pytest

from numeric_matrix_processor.matrix import Matrix

SINGLE_VALUE_MATRIX = [1, [1], [[1]]]
SINGLE_VALUE_MATRIX_SHAPE = [(1, 1)]

LINE_MATRIX = [[3.43, 5.643, 3234, -2334.4324]]
LINE_MATRIX_SHAPE = [(1, 4)]

COLUMN_MATRIX = [[[1], [-3], [4.543], [0], [323.532], [-34214.442]]]
COLUMN_MATRIX_SHAPE = [(6, 1)]

SQUARE_MATRIX = [[[1, 2, 3, 4], [5, 6 ,7, 8],[1, 2, 3, 4], [5, 6 ,7, 8]]]
SQUARE_MATRIX_SHAPE = [(4, 4)]

GENERIC_MATRIX = [[[1, 2, 3, 4], [5, 6 ,7, 8]]]
GENERIC_MATRIX_SHAPE = [(2, 4)]

matrixes_parameters = pytest.mark.parametrize("value, shape",
                                              list(product(SINGLE_VALUE_MATRIX, SINGLE_VALUE_MATRIX_SHAPE))
                                              + list(product(LINE_MATRIX, LINE_MATRIX_SHAPE))
                                              + list(product(COLUMN_MATRIX, COLUMN_MATRIX_SHAPE))
                                              + list(product(SQUARE_MATRIX, SQUARE_MATRIX_SHAPE))
                                              + list(product(GENERIC_MATRIX, GENERIC_MATRIX_SHAPE))
                                              )

@matrixes_parameters
def test_lines_count(value, shape):
    matrix = Matrix(value)
    assert shape[0] == matrix.get_lines()

@matrixes_parameters
def test_lines_count(value, shape):
    matrix = Matrix(value)
    assert shape[1] == matrix.get_columns()

@matrixes_parameters
def test_lines_values(value, shape):
    matrix = Matrix(value)
    assert shape[1] == matrix.get_columns()

@pytest.mark.parametrize("value", ["1", ["1"], [[1, 2], [1]], [[1, 2], [1, "2"]], ])
def test_invalid_entries(value):
    with pytest.raises(ValueError):
        Matrix(value)
