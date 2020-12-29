import sys

from numeric_matrix_processor.matrix import Matrix

__ADD__MATRICES = 1
__MULTIPLY_BY_CONSTANT = 2
__MULTIPLE_BY_MATRIX = 3
__EXIT = 0


def ask_for_task_choice():
    """Print choice menu and register user answer"""
    message = "{}. Add matrices\n{}. Multiply matrix by a constant\n{}. Multiply matrices\n{}. Exit\nYour choice: ".format(
        __ADD__MATRICES,
        __MULTIPLY_BY_CONSTANT,
        __MULTIPLE_BY_MATRIX,
        __EXIT
    )

    return int(input(message))


def process_choice(value):
    """Process user input"""
    if value == __ADD__MATRICES:
        addition()
    elif value == __MULTIPLY_BY_CONSTANT:
        scalar_multiplication()
    elif value == __MULTIPLE_BY_MATRIX:
        matrices_multiplications()
    elif value == __EXIT:
        sys.exit()
    else:
        print("Invalid choice")


def addition():
    """Perform the matrix addition task"""
    m_matrix = Matrix(ask_for_matrix("Enter size of first matrix: ", "Enter first matrix:\n"))
    n_matrix = Matrix(ask_for_matrix("Enter size of second matrix: ", "Enter second matrix:\n"))

    print("The result is:\n{}".format(m_matrix + n_matrix))


def scalar_multiplication():
    """Perform the scalar multiplication task"""
    m_matrix = Matrix(ask_for_matrix("Enter size of matrix: ", "Enter matrix:\n"))
    n_matrix = float(input("Enter constant: "))

    print("The result is:\n{}".format(m_matrix * n_matrix))


def matrices_multiplications():
    """Perform the matrices multiplication task"""
    m_matrix = Matrix(ask_for_matrix("Enter size of first matrix: ", "Enter first matrix:\n"))
    n_matrix = Matrix(ask_for_matrix("Enter size of second matrix: ", "Enter second matrix:\n"))

    print("The result is:\n{}".format(m_matrix * n_matrix))


def ask_for_matrix(initial_message, second_message):
    """Obtain an input in the way supported by the task"""

    def take_input(message, type_of_value):
        return (type_of_value(x) for x in input(message).split())

    n, _ = take_input(initial_message, int)
    values = [list(take_input(second_message if i == 0 else '', float)) for i in range(n)]
    return values


if __name__ == "__main__":
    while True:
        choice = ask_for_task_choice()
        process_choice(choice)
