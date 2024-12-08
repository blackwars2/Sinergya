a = int(input("Введи пятизначное число: "))
one = a % 10
tens = (a // 10) % 10
hundreds = (a // 100) % 10
thousands = (a // 1000) % 10
tens_of_thousands = (a // 10000) % 10

res_1 = tens ** one
res_2 = (res_1 * hundreds) / (tens_of_thousands - thousands)
print(res_2)