m, n = map(int,input().split())
d = [0] * m
for i in range(n):
    a,b,c = map(int,input().split())
    for x in range(a-1,b):
        d[x] = c
for y in range(0,m):
    print(d[y], end=" ")