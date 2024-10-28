def divide(first, second):

    if second != 0:
        result = first / second
        return result
    else:
        return 'Ошибка'


result1 = divide(69, 3)
try:
    result2 = divide(3, 0)
except ZeroDivisionError:
    print('Ошибка')

if __name__ == '__main__':
    print(result1)
    print(result2)

