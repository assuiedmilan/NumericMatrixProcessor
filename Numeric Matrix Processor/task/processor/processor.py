from numeric_matrix_processor.matrix import Matrix


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
