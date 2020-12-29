import pytest

from numeric_matrix_processor.matrix import Matrix


# noinspection PyTypeChecker
@pytest.mark.parametrize("first, second, result", [
    (Matrix(1), Matrix(2), Matrix(3)),
    (Matrix([[1]]), Matrix([[2]]), Matrix([[3]])),
    (Matrix([[1, 2, 3], [4, 5, 6]]), Matrix([[4, 5, 6], [1, 2, 3]]), Matrix([[5, 7, 9], [5, 7, 9]])),
    pytest.param(Matrix(1), Matrix([1, 2]), Matrix(3), marks=pytest.mark.xfail(raises=ValueError, strict=True))
])
def test_addition(first, second, result):
    """Test matrix additions"""
    assert result == (first + second)


# noinspection PyTypeChecker
@pytest.mark.parametrize("first, second, result", [
    (Matrix(1), Matrix(2), Matrix(-1)),
    (Matrix([[1]]), Matrix([[2]]), Matrix([[-1]])),
    (Matrix([[1, 2, 3], [4, 5, 6]]), Matrix([[4, 5, 6], [1, 2, 3]]), Matrix([[-3, -3, -3], [3, 3, 3]])),
    pytest.param(Matrix(1), Matrix([1, 2]), Matrix(3), marks=pytest.mark.xfail(raises=ValueError, strict=True))
])
def test_subtraction(first, second, result):
    """Test matrix subtraction"""
    assert result == (first - second)


@pytest.mark.parametrize("first, second, result", [
    (Matrix([[1, 2, 3], [4, 5, 6]]), Matrix([[7, 8], [9, 10], [11, 12]]), Matrix([[58, 64], [139, 154]])),
    (
            Matrix([[1, 4, 5, 6, 6], [7, 8, 9, 0, 0], [4, 1, 2, 2, 2]]),
            Matrix([[4, 5], [6, 1], [6, 0], [0, 9], [7, 7]]),
            Matrix([[100, 105], [130, 43], [48, 53]])
    ),
    pytest.param(
        Matrix([[1, 4, 5, 6], [7, 8, 9, 0], [4, 1, 2, 2]]),
        Matrix([[4, 5], [6, 1], [6, 0], [0, 9], [7, 7]]),
        Matrix([[100, 105], [130, 43], [48, 53]]),
        marks=pytest.mark.xfail(raises=ValueError, strict=True)
    )
])
def test_multiplication(first, second, result):
    """Test matrix multiplication"""
    assert result == (first * second)
