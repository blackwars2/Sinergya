
def start(x):
    return (x % 3)

cmp = [15, 22 ,8, 9, 13, 33]
cmp.sort(key=start)
print(cmp)