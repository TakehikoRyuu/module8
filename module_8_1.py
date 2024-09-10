# Try и Except
def add_everything_up(a, b):
    try:
        result = a+b
        return round(result, 3)
    except (TypeError):
        a_1 = str(a)
        b_1 = str(b)
        result = a_1 + b_1
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))