m = int(input("Введите максимальный вес лодки: "))
n = int(input("Введите количество рыбаков: "))
boat = 0
weight = []
if (n >= 1) and (n <= 100):
    for i in range(n):
        a = int(input(("Введите вес рыбака: ")))
        weight.append(a)
print(weight)

i = 0
while i < len(weight):
    if i + 1 <  len(weight) and (weight [i] + weight [i +1]) <= m:
        boat +=1
        i +=2
    else:
        boat +=1
        i += 1
print(boat)

