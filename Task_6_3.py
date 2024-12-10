A = int(input("Введи натуральное число A: "))
B = int(input("Введи натуральное число B: "))
for i in range (A, B+1, 1):
    if i % 2 == 0:
        print(i, end =" ")
