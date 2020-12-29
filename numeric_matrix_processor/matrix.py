from operator import add
from operator import mul
from operator import sub
from typing import List


class Matrix:
    """Basic definition of a matrix

    Valid entries are:
        A list of lists of int/floats that defines a matrix
        A list of int/floats that defines a line matrix
        An int/float that define a single value matrix

        Args:
            value (List[list]): A list of list of ints/floats defining a matrix

        Attributes:
            value (List[list]): A list of list of ints/floats defining the matrix
    """

    def __init__(self, value: List[list]):
        self.__value = value
        self.__validate()

    @property
    def value(self):
        """Return the matrix value"""
        return self.__value

    @property
    def shape(self):
        """Shape of the matrix"""
        return self.get_lines_count(), self.get_columns_count()

    def __getitem__(self, item):
        """Redefine [] so it can receive a tuple in a 'Matlab' fashion"""
        return self.value[item[0]][item[1]]

    def __setitem__(self, key, value):
        """Redefine [] so it can assign a value via a tuple in a 'Matlab' fashion"""
        self.value[key[0]][key[1]] = value

    def __repr__(self):
        return "".join([" ".join([str(i) for i in line]) + "\n" for line in self.value])

    def __eq__(self, other):
        return list(self.get_lines()) == list(other.get_lines())

    def __add__(self, other):
        return self.__addition_law(other, add)

    def __sub__(self, other):
        return self.__addition_law(other, sub)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__multiply_by_number(other)

        if isinstance(other, Matrix):
            return self.__multiply_by_matrix(other)

        raise ValueError("Multiplication is allowed only by scalar or Matrices")

    def get_lines_count(self) -> int:
        """Returns the number of lines"""
        return len(self.value)

    def get_columns_count(self) -> int:
        """Returns the number of columns"""
        return len(self.value[0])

    def get_lines(self):
        """Returns lines as an iterator"""
        for i in range(self.get_lines_count()):
            yield self.value[i]

    def get_columns(self):
        """Returns columns as an iterator"""
        for i in range(self.get_columns_count()):
            yield [x[i] for x in self.value]

    def __multiply_by_number(self, number):
        """Apply scalar multiplication to the matrix"""
        new_values = [[value * number for value in line] for line in self.get_lines()]
        return Matrix(new_values)

    def __multiply_by_matrix(self, other):

        def compute_single_value(processed_line, processed_column):
            return sum(map(lambda x: mul(x[0], x[1]), zip(processed_line, processed_column)))

        if self.get_columns_count() != other.get_lines_count():
            raise ValueError("Matrices to add must have compatibles sizes.\n - Self matrix is {}\n - Other matrix is {}".format(self.shape, other.shape))

        values = [
            [compute_single_value(line, column) for column in other.get_columns()]
            for line in self.get_lines()
        ]

        return Matrix(values)

    def __addition_law(self, other, operation):
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
