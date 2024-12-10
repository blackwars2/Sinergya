n = int(input("Введи количество вводимых чисел: "))
cnt = 0
for i in range(1, n+1):
    a = int(input("Введи число: "))
    if a == 0:
        cnt += 1
print(cnt)

