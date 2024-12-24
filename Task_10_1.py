pets = {}

while True:
    a = input("Введите имя питомца: ")
    if a == '':
        break
    else:
        a1 = input('Вид питомца: ')
        a2 = int(input('Возраст питомца: '))

    year_case = ''
    if a2 % 10 == 1 and a2 != 11 and a2 % 100 != 11:
        year_case = 'год'
    elif 1 < a2 % 10 <= 4 and a2 != 12 and a2 != 13 and a2 != 14:
        year_case = 'года'
    else:
        year_case = 'лет'

    a3 = input("Имя владельца: ")

    pets[a] = {'Вид питомца': a1, 'Возраст питомца': a2, 'Имя владельца': a3}

for pet_name, details in pets.items():
    print("Это", details['Вид питомца'], "по кличке", pet_name,
          "Возраст питомца:", details['Возраст питомца'], year_case,
          "Имя владельца:", details['Имя владельца'])