def input_f():
    while True:
        n = int(input('Введите натуральное число'))
        if n > 0:
            break
        print('Неверные даные')
    return n










def collatz(n):
    result = [n]
    if n == 1:
        pass
    elif n % 2 == 0:
        result.extend(x2(n))
    else:
        result.extend(x3_1(n))
    return result
