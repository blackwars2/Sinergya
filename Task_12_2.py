from itertools import count

list = [5, 22, 15, 55, 4, 2, 9, 2, 4, 15]

count = 0

n = len(list)

for i in range (n):
    for j in range(n-1-i):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1], list[j]

print(list)


for i in range (n-1):
    if list[i] != list[i+1]:
        count += 1


count += 1
print(count)