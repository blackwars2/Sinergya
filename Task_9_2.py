s1 = input()
s2 = input()

s1 = s1.split()
s2 = s2.split()

s1 = set(s1)
s2 = set(s2)

print(s1)
print(s2)
cnt = 0
for i in s1:
    if i in s2:
        cnt += 1
    else:
        cnt += 0
print(cnt)