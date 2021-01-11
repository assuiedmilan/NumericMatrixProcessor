import pytest

from numeric_matrix_processor.matrix import Matrix

SINGLE_VALUE_MATRIX = [1, [1], [[1]]]
SINGLE_VALUE_MATRIX_SHAPE = (1, 1)
SINGLE_VALUE_MATRIX_LINES = [[1]]
SINGLE_VALUE_MATRIX_COLUMNS = [[1]]

LINE_MATRIX = [[3.43, 5.643, 3234, -2334.4324], [[3.43, 5.643, 3234, -2334.4324]], ]
LINE_MATRIX_SHAPE = (1, 4)
LINE_MATRIX_LINES = [[3.43, 5.643, 3234, -2334.4324]]
LINE_MATRIX_COLUMNS = [[3.43], [5.643], [3234], [-2334.4324]]

COLUMN_MATRIX = [[[1], [-3], [4.543], [0], [323.532], [-34214.442]]]
COLUMN_MATRIX_SHAPE = (6, 1)
COLUMN_MATRIX_LINES = [[1], [-3], [4.543], [0], [323.532], [-34214.442]]
COLUMN_MATRIX_COLUMNS = [[1, -3, 4.543, 0, 323.532, -34214.442]]

SQUARE_MATRIX = [[[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]]
SQUARE_MATRIX_SHAPE = (4, 4)
SQUARE_MATRIX_LINES = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
SQUARE_MATRIX_COLUMS = [[1, 5, 1, 5], [2, 6, 2, 6], [3, 7, 3, 7], [4, 8, 4, 8]]

GENERIC_MATRIX = [[[1, 2, 3, 4], [5, 6, 7, 8]]]
GENERIC_MATRIX_SHAPE = (2, 4)
GENERIC_MATRIX_LINES = [[1, 2, 3, 4], [5, 6, 7, 8]]
GENERIC_MATRIX_COLUMNS = [[1, 5], [2, 6], [3, 7], [4, 8]]

__all_matrixes = [
    SINGLE_VALUE_MATRIX,
    LINE_MATRIX,
    COLUMN_MATRIX,
    SQUARE_MATRIX,
    GENERIC_MATRIX,
]


def __generator(*args):
    for i, v in enumerate(args):
        for matrix_format in __all_matrixes[i]:
            yield matrix_format, v


matrixes = pytest.mark.parametrize("value", SINGLE_VALUE_MATRIX + LINE_MATRIX + COLUMN_MATRIX + SQUARE_MATRIX + GENERIC_MATRIX)
matrixes_shapes = pytest.mark.parametrize("value, shape", list(__generator(SINGLE_VALUE_MATRIX_SHAPE, LINE_MATRIX_SHAPE, COLUMN_MATRIX_SHAPE, SQUARE_MATRIX_SHAPE, GENERIC_MATRIX_SHAPE)))
matrixes_lines = pytest.mark.parametrize("value, lines", list(__generator(SINGLE_VALUE_MATRIX_LINES, LINE_MATRIX_LINES, COLUMN_MATRIX_LINES, SQUARE_MATRIX_LINES, GENERIC_MATRIX_LINES)))
matrixes_columns = pytest.mark.parametrize("value, columns", list(__generator(SINGLE_VALUE_MATRIX_COLUMNS, LINE_MATRIX_COLUMNS, COLUMN_MATRIX_COLUMNS, SQUARE_MATRIX_COLUMS, GENERIC_MATRIX_COLUMNS)))


@matrixes
def test_format(value):
    """Test that returned matrix value is always a list"""
    matrix = Matrix(value)
    assert isinstance(matrix.value, list)


@matrixes_shapes
def test_shape(value, shape):
    """Test shape property"""
    matrix = Matrix(value)
    assert shape == matrix.shape


@matrixes_shapes
def test_lines_count(value, shape):
    """Test lines count"""
    matrix = Matrix(value)
    assert shape[0] == matrix.get_lines_count()


@matrixes_lines
def test_lines(value, lines):
    """Test that lines are correctly represented"""
    matrix = Matrix(value)
    assert lines == list(matrix.get_lines())


@matrixes_shapes
def test_colums_count(value, shape):
    """Test lines count"""
    matrix = Matrix(value)
    assert shape[1] == matrix.get_columns_count()


@matrixes_columns
def test_columns(value, columns):
    """Test that columns are correctly represented"""
    matrix = Matrix(value)
    assert columns == list(matrix.get_columns())


@pytest.mark.parametrize("value", [[], "1", ["1"], [[1, 2], [1]], [[1, 2], [1, "2"]], ])
def test_invalid_entries(value):
    """Test invalid entries"""
    with pytest.raises(ValueError):
        Matrix(value)
