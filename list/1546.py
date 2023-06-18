a = int(input())
l = [0] * a
b = [0] * len(l)
c = 0
k = list(map(int,input().split()))
for i in range(len(l)):
    l[i] = k
    
for x in range(len(l)):
    b[x] = l[x] / max(l) * 100
for y in range(len(b)):
    c += b[y]
c = c / len(b)
print(c)