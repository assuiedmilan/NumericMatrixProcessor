from typing import List


class Matrix:

    def __init__(self, value: List[list]):
        """

        Returns:
            object: 
        """
        self.value = value
        self.__validate()


    def get_lines(self) -> int:
        return len(self.value)

    def get_columns(self) -> int:
        return len(self.value[0])

    def __validate(self):

        value = self.value

        if not isinstance(value, list):
            if not isinstance(value, int) and not isinstance(value, float):
                raise ValueError("Argument is not a matrix of numerical value, nor a single value, but a {}".format(type(value)))
            else:
                self.value = [[value]]

        else:

            first_line = value[0]

            if not isinstance(first_line, list):
                if not isinstance(first_line, int) and not isinstance(first_line, float):
                    raise ValueError("First line is not a list of numerical value, nor a single value, but a {}".format(type(first_line)))
                else:
                    self.value = [first_line]

            else:

                for line in value:
                    if not isinstance(line, list):
                        raise ValueError("Line is not a list of numerical value, nor a single value, but a {}".format(type(first_line)))
                    elif len(line) != len(first_line):
                        raise ValueError("Lines does not have the same length. First line has a length of {}, vs {}".format(len(line), len(first_line)))

