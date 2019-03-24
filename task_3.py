def test_task_3():
    test_lucky_matrix = [
        [[1, 2, 3, 4],
         [2, 3, 4, 1],
         [3, 4, 1, 2],
         [4, 1, 2, 1]],
        [[1, 1, 1, 1],
         [0, 3, 1, 1],
         [0, 0, 1, 1],
         [6, 0, 0, 1]],
        [[1, 1, 1, -1],
         [0, 3, 1, 1],
         [0, 0, 1, 1],
         [4, 0, 0, 1]],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    ]
    test_unlucky_matrix = [
        [[1, 2, 3, 4],
         [2, 3, 4, 1],
         [3, 4, 1, 2],
         [4, 1, 7, 1]],
        [[9, 9, 9, 4],
         [9, 9, 3, 9],
         [9, 2, 9, 9],
         [1, 9, 9, 9]]
    ]

    print("\nПроверка задания №3:")
    for matrix in test_lucky_matrix:
        if not is_lucky(matrix):
            print("Ошибка. Проверяемый квадрат: ", matrix,
                  ".Ожидаемый результат: True. Полученный результат: False")
    for matrix in test_unlucky_matrix:
        if is_lucky(matrix):
            print("Ошибка. Проверяемый квадрат: ", matrix,
                  ". Ожидаемый результат: False. Полученный результат: True")


def is_lucky(matrix: list) -> bool:
    avg = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                avg += matrix[i][j]
            if j > i:
                avg -= matrix[i][j]
        if i == len(matrix) - 1:
            if avg == 0:
                print(matrix[i], " - \"счастливый\" квадрат")
            else:
                print(matrix[i], " - не \"счастливый\" квадрат")
        else:
            print(matrix[i])
    return avg == 0


test_task_3()
