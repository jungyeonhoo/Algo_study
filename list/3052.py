l = [0] * 10
b = [0] * 10
for i in range(10):
    k = int(input())
    l[i] = k 
for a in range(10):
    b[a] = l[a] % 42
b = set(b)
print(len(b))

