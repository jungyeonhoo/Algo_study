a = int(input())
l = [0] * a
b = [0] * a
c = 0
k = list(map(int,input().split()))
for i in range(a):
    l[i] = k[i]
    
for x in range(a):
    b[x] = l[x] / max(l) * 100
for y in range(len(b)):
    c += b[y]
c = c / len(b)
print(c)