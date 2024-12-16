n1 = int(input())
cl = set()
for i in range(n1):
    n2 = input()
    if n2 in cl:
        print("Sorry The number is already cl")
    else:
        cl.add(n2)
ctn = 0
for i in cl:
    ctn += 1
print(ctn)