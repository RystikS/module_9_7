def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result >= 2:
            for i in range(2, result + 1):
                if result % i == 0:
                    print('Составное')
                    return result
                else:
                    print('Простое')
                    return result
        else:
            print('Не является ни простым, ни составным числом')  # Ситуация при котором сумма трех числе равна 1
            return result

    return wrapper


@is_prime
def sum_three(x, y, z):
    return x + y + z


result = sum_three(2, 0, 6)
print(result)
