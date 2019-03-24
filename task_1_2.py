def test_task_1():
    test_numbers = {
        55: True,
        -55: True,
        2121: True,
        367763: True,
        367367: True,
        21: False,
        12: False,
        -12: False,
        1215: False,
        186953: False
    }

    print("\nПроверка задания №1:")
    for number in test_numbers:
        expected = test_numbers[number]
        actual = is_lucky(number)
        if expected != actual:
            print("Ошибка. Проверяемый набор: ", number,
                  ". Ожидаемый результат: ", expected,
                  ". Полученный результат: ", actual)


def test_task_2():
    test_numbers = {
        0: True,
        1: True,
        -1: True,
        565: True,
        21221: True,
        3679763: True,
        123: False,
        -281: False,
        12315: False,
        1864953: False
    }

    print("\nПроверка задания №2:")
    for number in test_numbers:
        expected = test_numbers[number]
        actual = is_lucky(number)
        if expected != actual:
            print("Ошибка. Проверяемый набор: ", number,
                  ". Ожидаемый результат: ", expected,
                  ". Полученный результат: ", actual)


def is_lucky(number: int) -> bool:
    number_str = str(abs(number))
    avg = 0
    i = 0
    j = len(number_str) - 1
    while i < j:
        avg += int(number_str[i]) - int(number_str[j])
        i += 1
        j -= 1
    if avg == 0:
        print(number, " - \"счастливый\" набор")
    else:
        print(number, " - не \"счастливый\" набор")
    return avg == 0


test_task_1()
test_task_2()
