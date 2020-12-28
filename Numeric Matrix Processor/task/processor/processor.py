from numeric_matrix_processor.matrix import Matrix


def receive_input():
    def take_input(message):
        return (int(x) for x in input("{} ".format(message)).split())

    def take_line(line_index, number_of_columns):
        value = [x for x in take_input("Row {}:".format(line_index))]

        if len(value) != number_of_columns:
            raise ValueError("Input is invalid, expected {} values per line".format(number_of_columns))

        return value

    n, m = take_input("Enter number of rows and columns:")
    values = [take_line(i, m) for i in range(n)]
    return values


if __name__ == "__main__":
    v = receive_input()
    l = Matrix(v)
