def input_f():
    while True:
        n = int(input('Введите натуральное число'))
        if n > 0:
            break
        print('Неверные даные')
    return n
