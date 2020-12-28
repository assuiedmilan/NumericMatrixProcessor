from operator import add
from typing import List


class Matrix:
    """Basic definition of a matrix

    Valid entries are:
        A list of lists of int/floats that defines a matrix
        A list of int/floats that defines a line matrix
        An int/float that define a single value matrix

        Note:
            This version is stripped of all non task specific code

        Args:
            value (List[list]): A list of list of ints/floats defining a matrix

        Attributes:
            value (List[list]): A list of list of ints/floats defining the matrix
    """

    def __init__(self, value: List[list]):
        self.__value = value

    @property
    def value(self):
        """Return the matrix value"""
        return self.__value

    @property
    def shape(self):
        """Shape of the matrix"""
        return self.get_lines_count(), self.get_columns_count()

    def __repr__(self):
        return "".join([" ".join([str(i) for i in line]) + "\n" for line in self.value])

    def __add__(self, other):
        if self.shape != other.shape:
            return "ERROR"

        return Matrix(list(map(lambda x: list(map(add, x[0], x[1])), zip(self.get_lines(), other.get_lines()))))

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


def receive_input():
    """Obtain an input in the way supported by the task"""
    def take_input():
        return (int(x) for x in input().split())

    n, _ = take_input()
    values = [list(take_input()) for _ in range(n)]
    return values


if __name__ == "__main__":
    m_matrix = Matrix(receive_input())
    n_matrix = Matrix(receive_input())

    print(m_matrix + n_matrix)
