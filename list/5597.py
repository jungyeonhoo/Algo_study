l = [0] * 30

for i in range(28):
    k = int(input())
    l[k-1] = 1

for i in range(len(l)):
    if l[i] == 0:
        print(i+1)