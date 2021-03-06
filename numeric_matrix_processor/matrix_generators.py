from numeric_matrix_processor.matrix import Matrix


def get_identity(size: int) -> 'Matrix':
    """Generates an Identity Matrix

    Args:
        size(int): the size of the requested Matrix

    Returns:
        An Identify Matrix
    """

    values = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    return Matrix(values)
