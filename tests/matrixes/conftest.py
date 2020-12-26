from itertools import product

import pytest

SINGLE_VALUE_MATRIX = [1, [1], [[1]]]
SINGLE_VALUE_MATRIX_SHAPE = [(1, 1)]
SINGLE_VALUE_MATRIX_LINES = [1]
SINGLE_VALUE_MATRIX_COLUMNS = [1]

LINE_MATRIX = [[3.43, 5.643, 3234, -2334.4324], [[3.43, 5.643, 3234, -2334.4324]], ]
LINE_MATRIX_SHAPE = [(1, 4)]
LINE_MATRIX_LINES = [3.43, 5.643, 3234, -2334.4324]
LINE_MATRIX_COLUMNS = [[3.43], [5.643], [3234], [-2334.4324]]

COLUMN_MATRIX = [[[1], [-3], [4.543], [0], [323.532], [-34214.442]]]
COLUMN_MATRIX_SHAPE = [(6, 1)]
COLUMN_MATRIX_LINES = [[1], [-3], [4.453], [0], [323.532], [-34214.442]]
COLUMN_MATRIX_COLUMNS = [1, -3, 4.453, 0, 323.532, -34214.442]

SQUARE_MATRIX = [[[1, 2, 3, 4], [5, 6 ,7, 8],[1, 2, 3, 4], [5, 6 ,7, 8]]]
SQUARE_MATRIX_SHAPE = [(4, 4)]
SQUARE_MATRIX_LINES = [[1, 2, 3, 4], [5, 6 ,7, 8], [1, 2, 3, 4], [5, 6 ,7, 8]]
SQUARE_MATRIX_COLUMS = [[1, 5, 1, 5], [2, 6, 2, 6], [3, 7, 3, 7], [4, 8, 4, 8]]

GENERIC_MATRIX = [[[1, 2, 3, 4], [5, 6 ,7, 8]]]
GENERIC_MATRIX_SHAPE = [(2, 4)]
GENERIC_MATRIX_LINES = [[1, 2, 3, 4], [5, 6 ,7, 8]]
GENERIC_MATRIX_COLUMNS = [[1, 5], [2, 6], [3, 7], [4, 8]]

matrixes = pytest.mark.parametrize("value", SINGLE_VALUE_MATRIX + LINE_MATRIX + COLUMN_MATRIX + SQUARE_MATRIX + GENERIC_MATRIX)

matrixes_shapes = pytest.mark.parametrize("value, shape",
                                          list(product(SINGLE_VALUE_MATRIX, SINGLE_VALUE_MATRIX_SHAPE))
                                          + list(product(LINE_MATRIX, LINE_MATRIX_SHAPE))
                                          + list(product(COLUMN_MATRIX, COLUMN_MATRIX_SHAPE))
                                          + list(product(SQUARE_MATRIX, SQUARE_MATRIX_SHAPE))
                                          + list(product(GENERIC_MATRIX, GENERIC_MATRIX_SHAPE))
                                          )

matrixes_lines = pytest.mark.parametrize("value, lines",
                                          list(product(SINGLE_VALUE_MATRIX, SINGLE_VALUE_MATRIX_LINES))
                                          + list(product(LINE_MATRIX, LINE_MATRIX_LINES))
                                          + list(product(COLUMN_MATRIX, COLUMN_MATRIX_LINES))
                                          + list(product(SQUARE_MATRIX, SQUARE_MATRIX_LINES))
                                          + list(product(GENERIC_MATRIX, GENERIC_MATRIX_LINES))
                                          )

matrixes_columns = pytest.mark.parametrize("value, columns",
                                          list(product(SINGLE_VALUE_MATRIX, SINGLE_VALUE_MATRIX_COLUMNS))
                                          + list(product(LINE_MATRIX, LINE_MATRIX_COLUMNS))
                                          + list(product(COLUMN_MATRIX, COLUMN_MATRIX_COLUMNS))
                                          + list(product(SQUARE_MATRIX, SQUARE_MATRIX_COLUMS))
                                          + list(product(GENERIC_MATRIX, GENERIC_MATRIX_COLUMNS))
                                          )
