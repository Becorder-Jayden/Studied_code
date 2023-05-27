n = int(input())
lis = []

for i in range(n):
    m = int(input())
    lis.append(m)

a = sorted(lis)
for i in a:
    print(i)