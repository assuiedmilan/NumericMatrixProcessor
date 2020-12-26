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

    def get_lines_count(self) -> int:
        """Returns the number of lines"""
        return len(self.__value)

    def get_columns_count(self) -> int:
        """Returns the number of columns"""
        return len(self.__value[0])

    def get_lines(self):
        """Returns lines as an iterator"""
        for i in range(self.get_lines_count()):
            yield self.__value[i]

    def get_columns(self):
        """Returns columns as an interator"""
        for i in range(self.get_columns_count()):
            yield [x[i] for x in self.__value]



    def __validate(self):

        def is_line_valid(line_under_test):
            return all(isinstance(x, (int, float)) for x in line_under_test)

        value = self.__value

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
