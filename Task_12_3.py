n = 5 # Сотрудников
sph = [2, 20, 5, 3, 4] # Сколько сотрудник получает за час
hs = [5, 6, 20, 13, 4] # Скоько сотрудник отработал за час

res = []

for i in range(n):
    r = sph[i] * hs[i]
    res.append(r)

res.sort()

print(res)