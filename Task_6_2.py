x = int(input("Введи натуральное число x: "))
cnt = 0
for i in range(1, x+1):
    if x % i == 0:
        cnt += 1
print(cnt)