s = input()
s = s.split()
s2 = set()

for i in s:
    if i in s2:
        print(f'{i} YES')
    else:
        print(f'{i} NO')
    s2.add(i)