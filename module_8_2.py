# Сложные моменты и исключения в стеке вызовов функции

def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    ret = (result, incorrect_data)
    return ret


def calculate_average(numbers):
    try:
        sum_numbers = personal_sum(numbers)
        len_numbers = 0
        for i in numbers:
            if isinstance(i, int) or isinstance(i, float):
                len_numbers += 1
        return sum_numbers[0] / len_numbers
    except ZeroDivisionError:
        return 0
    except TypeError:
        return print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать