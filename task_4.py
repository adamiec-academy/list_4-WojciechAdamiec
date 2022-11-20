def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(a, b):
    matrix = [["." for _ in range(a)] for _ in range(b)]
    x_size, y_size = len(matrix[0]), len(matrix)

    for y in range(y_size):
        matrix[y][0] = "X"
        matrix[y][x_size - 1] = "X"

    for x in range(x_size):
        matrix[0][x] = "X"
        matrix[y_size - 1][x] = "X"

    return matrix
