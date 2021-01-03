from operator import add
from operator import mul
from operator import sub
from typing import Generator
from typing import List
from typing import Tuple
from typing import Union


class Matrix:
    """Basic definition of a matrix

    Valid entries are:
        A list of lists of int/floats that defines a matrix
        A list of int/floats that defines a line matrix
        An int/float that define a single value matrix

        Args:
            value (List[List[float]]): A list of list of ints/floats defining a matrix

        Attributes:
            value (List[List[float]]): A list of list of ints/floats defining the matrix
    """

    __SINGLE_MATRIX = (1, 1)
    __TWO_TWO_MATRIX = (2, 2)

    def __init__(self, value: Union[List[List[float]], int, float]):  # pylint: disable=unsubscriptable-object
        self.__value = value
        self.__validate()

    @property
    def is_squared(self) -> bool:
        """Returns true if matrix is squared

        Returns:
            A boolean
        """

        return self.shape[0] == self.shape[1]

    @property
    def is_scalar(self) -> bool:
        """Returns true if matrix has size [1]

        Returns:
            A boolean
        """

        return self.__SINGLE_MATRIX == self.shape

    @property
    def is_two_by_two(self) -> bool:
        """Returns true if matrix has size [2, 2]

        Returns:
            A boolean
        """

        return self.__TWO_TWO_MATRIX == self.shape

    @property
    def value(self) -> List[list]:
        """Returns the matrix values

        Returns:
            The matrix values as a List[list]
        """

        return self.__value

    @property
    def shape(self) -> Tuple[int, int]:
        """Returns the shape of the matrix

        Returns:
            The shape of the matrix as a Tuple[int, int]
        """

        return self.get_lines_count(), self.get_columns_count()

    def __getitem__(self, item: Tuple[int, int]) -> float:
        """Redefines [] so it can receive a tuple in a 'Matlab' fashion

        Args:
            item (Tuple[int, int]): the matrix indexes

        Returns:
            The value in the matrix at the specified index, as an int or a float
        """

        return self.value[item[0]][item[1]]

    def __setitem__(self, key: Tuple[int, int], value: float):
        """Redefines [] so it can assign a value via a tuple in a 'Matlab' fashion

        Args:
            key (Tuple[int, int]): the matrix indexes
            value (int, float): the value to set
        """

        self.value[key[0]][key[1]] = value

    def __repr__(self) -> str:
        """Returns the string representation of the matrix

        Returns:
            A printable string
        """

        return "".join([" ".join([str(i) for i in line]) + "\n" for line in self.value])

    def __str__(self) -> str:
        """Returns a copiable and printable string representation of the matrix

        Returns:
            A copiable and printable string
        """
        return "Matrix([" + ", ".join("[" + ", ".join(str(x) for x in c) + "]" for c in self.value) + "])"

    def __eq__(self, other: 'Matrix') -> bool:
        """Returns true if both matrices are equal.

        Matrices are equal if they have the same shape and the same values

        Args:
            other (numeric_matrix_processor.matrix.Matrix): the matrix to compare with

        Returns:
            A boolean representing equality
        """

        return list(self.get_lines()) == list(other.get_lines())

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Returns matrices addition result

        Args:
            other (numeric_matrix_processor.matrix.Matrix): the matrix to add

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        return self.__addition_law(other, add)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Returns matrices substraction result

        Args:
            other (numeric_matrix_processor.matrix.Matrix): the matrix to substract

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        return self.__addition_law(other, sub)

    def __mul__(self, other: (int, float, 'Matrix')) -> 'Matrix':
        """Returns matrices addition result

        Args:
            other (numeric_matrix_processor.matrix.Matrix, int, float): the matrix to multiply with OR a scalar value

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        if isinstance(other, (int, float)):
            return self.__multiply_by_number(other)

        if isinstance(other, Matrix):
            return self.__multiply_by_matrix(other)

        raise ValueError("Multiplication is allowed only by scalar or Matrices")

    def transpose(self) -> 'Matrix':
        """Return transposed matrix

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        return Matrix(list(self.get_columns()))

    def side_transpose(self) -> 'Matrix':
        """Return transposed matrix over the side diagonal

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        return Matrix(list(reversed([list(reversed(column)) for column in self.get_columns()])))

    def vertical_transpose(self) -> 'Matrix':
        """Return transposed matrix over the vertical axis

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        return Matrix([list(reversed(line)) for line in self.get_lines()])

    def horizontal_transpose(self) -> 'Matrix':
        """Return transposed matrix over the horizontal axis

        Returns:
            A numeric_matrix_processor.matrix.Matrix
        """

        return Matrix(list(reversed(list(self.get_lines()))))

    def determinant(self) -> float:
        """Return the determinant value

        Returns:
            The determinant as a float
        """

        if self.__SINGLE_MATRIX == self.shape:
            return self[0, 0]

        return sum(
            cofactor * (squared_two_matrix[0, 0] * squared_two_matrix[1, 1] - squared_two_matrix[1, 0] * squared_two_matrix[0, 1])
            for cofactor, squared_two_matrix in self.get_reduced_minors()
        )

    def get_lines_count(self) -> int:
        """Returns the number of lines

        Returns:
            The number of lines as an int
        """

        return len(self.value)

    def get_columns_count(self) -> int:
        """Returns the number of columns

        Returns:
            The number of columns as an int
        """

        return len(self.value[0])

    def get_lines(self) -> Generator[List[float], None, None]:
        """Returns lines as an iterator

        Returns:
            A generator function iterating over the matrix lines
        """

        for i in range(self.get_lines_count()):
            yield self.value[i]

    def get_columns(self) -> Generator[List[float], None, None]:
        """Returns columns as an iterator

        Returns:
            A generator function iterating over the matrix columns
        """

        for i in range(self.get_columns_count()):
            yield [x[i] for x in self.value]

    def get_reduced_minors(self) -> Generator[Tuple[int, 'Matrix'], None, None]:
        """Returns a generator of all (cofactor, [2,2] minors) of the matrix using the first row

        Notes:
            All minors are decomposed until they are [2, 2] sized matrices.
            This will yield to n!/2! tuples of (cofactor, [2, 2] matrix)

        Returns:
            A generator functions of tuple(cofactor, minors)
        """

        cofactor = None

        if self.is_scalar or self.is_two_by_two:
            yield from self.get_minors()

        else:

            for minor in self.get_minors():
                cofactor = minor[0]
                minors = minor[1].get_reduced_minors()

                yield from map(lambda x: (x[0] * cofactor, x[1]), minors)

    def get_minors(self) -> Generator[Tuple[int, 'Matrix'], None, None]:
        """Returns a generator of all (cofactor, [n-1, n-n] minors) of the matrix using the first row

        Notes:
            This is the first decomposition so a [n, n] matrix will yield to n tuples of (cofactor, [n-1, n-1] matrix).

        Returns:
            A generator functions of tuple(cofactor, minors)
        """

        if self.is_scalar or self.is_two_by_two:
            yield self.get_minor_at(0, 0)
        else:
            for i in range(self.get_columns_count()):
                yield self.get_minor_at(0, i)

    def get_minor_at(self, line_index: int, column_index: int) -> Tuple[float, 'Matrix']:
        """Returns the cofactor and minor matrix at the specified index

        Args:
            line_index (int): line as a zero-based index
            column_index (int): column as a zero-based index

        Returns:
            A tuple(int, Matrix) containing the cofactor and the sub-matrix associated to the received indexes
        """

        if not self.is_squared:
            AttributeError("Minors can only be computed from squared matrix, current matrix has size ({})".format(self.shape))

        if self.is_scalar:
            return 1, Matrix(self[0, 0])

        if self.is_two_by_two:
            return 1, Matrix([[self[0, 0], self[0, 1]], [self[1, 0], self[1, 1]]])

        cofactor = (-1) ** (line_index + column_index) * self[line_index, column_index]

        sub_matrix = [line for i, line in enumerate(self.get_lines()) if i is not line_index]
        sub_matrix = [[column for j, column in enumerate(line) if j is not column_index] for line in sub_matrix]

        return cofactor, Matrix(sub_matrix)

    def __multiply_by_number(self, number: float) -> 'Matrix':
        """Apply scalar multiplication to the matrix"""
        new_values = [[value * number for value in line] for line in self.get_lines()]
        return Matrix(new_values)

    def __multiply_by_matrix(self, other: 'Matrix') -> 'Matrix':

        def compute_single_value(processed_line, processed_column):
            return sum(map(lambda x: mul(x[0], x[1]), zip(processed_line, processed_column)))

        if self.get_columns_count() != other.get_lines_count():
            raise ValueError("Matrices to add must have compatibles sizes.\n - Self matrix is {}\n - Other matrix is {}".format(self.shape, other.shape))

        values = [
            [compute_single_value(line, column) for column in other.get_columns()]
            for line in self.get_lines()
        ]

        return Matrix(values)

    def __addition_law(self, other: 'Matrix', operation: callable) -> 'Matrix':
        if self.shape != other.shape:
            raise ValueError("Matrices to add must have the same size.\n - Self matrix is {}\n - Other matrix is {}".format(self.shape, other.shape))

        return Matrix(list(map(lambda x: list(map(operation, x[0], x[1])), zip(self.get_lines(), other.get_lines()))))

    def __validate(self):

        def is_line_valid(line_under_test):
            return all(isinstance(x, (int, float)) for x in line_under_test)

        value = self.value

        if not isinstance(value, list):
            if not is_line_valid([value]):
                raise ValueError("Argument is not a matrix of numerical value, nor a single value, but a {}".format(type(value)))

            self.__value = [[value]]

        else:

            first_line = value[0]

            if not isinstance(first_line, list):
                if not is_line_valid([first_line]):
                    raise ValueError("First line is not a list of numerical value, nor a single value, but a {}".format(type(first_line)))

                self.__value = [value]

            else:

                for line in value:
                    if not isinstance(line, list):
                        raise ValueError("Line is not a list of numerical value, but a {}".format(type(first_line)))

                    if len(line) != len(first_line):
                        raise ValueError("Lines does not have the same length. First line has a length of {}, vs {}".format(len(line), len(first_line)))

                    if not is_line_valid(line):
                        raise ValueError("Lines line is not a list of numerical value, verify all values in {}".format(type(line)))
