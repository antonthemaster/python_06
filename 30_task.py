a = int(input('Enter first element (number): '))
n = int(input('Enter quantity: '))
d = int(input('Enter diff: '))
res = [a]

for i in range(2, n + 1):
    res.append(a + (i-1) * d)
print(res)
