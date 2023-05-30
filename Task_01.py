# Напишите функцию для транспонирования матрицы

# матрица для транспонирования
MATRIX = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
]


def main():
    print("Исходная матрица:")
    print_matrix(MATRIX)
    print("Транспонированная:")
    print_matrix(transpose_matrix(MATRIX))


def print_matrix(matr: list[list]):
    """Вывод квадратной матрицы на экран"""
    for row in matr:
        print(row)


def transpose_matrix(matr: list[list]) -> list[list]:
    """Транспонирование матрицы"""
    new_matr = [[] for _ in range(0, len(matr[0]))]
    for row in range(len(matr)):
        for col in range(len(matr[row])):
            new_matr[col].append(matr[row][col])
    return new_matr


if __name__ == "__main__":
    main()
