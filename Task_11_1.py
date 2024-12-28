def start(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * start(n - 1)

def list(num):
    one_factorial = start(num)
    res = []

    for i in range(one_factorial, 0, -1):
        res.append(start(i))
    return res

number = int(input("Введи число: "))
print(list(number))