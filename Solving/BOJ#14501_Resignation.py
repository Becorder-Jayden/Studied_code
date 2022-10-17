import sys
sys.stdin = open('BOJ#14501_Resignation.txt')

N = int(input())
T = []
P = []
for n in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    print(i+T[i])

print(T)
print(P)
