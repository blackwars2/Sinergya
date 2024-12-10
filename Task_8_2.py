n = int(input())
list = []
for i in range(n):
    a = int(input())
    if a >= 1 and a <= 100000:
        list.append(a)
    else:
        print("Введите верное число")
a = list.pop(-1)
list.insert(0, a)
print(list)