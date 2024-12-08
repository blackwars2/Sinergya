slovo = input("Введите слово: ")
a=slovo.count('a')
e=slovo.count('e')
i=slovo.count('i')
o=slovo.count('o')
u=slovo.count('u')

sumglass=a+e+i+o+u

print("Всего гласных",sumglass)
if (a == 0):
    print("Гласной а в слове нет")
else:
    print("a=", a)
if (e == 0):
    print("Гласной e в слове нет")
else:
    print("e=", e)
if (i == 0):
    print("Гласной i в слове нет")
else:
    print("i=", i)
if (o == 0):
    print("Гласной o в слове нет")
else:
    print("o=", o)
if (u == 0):
    print("Гласной u в слове нет")
else:
    print("u=", u)