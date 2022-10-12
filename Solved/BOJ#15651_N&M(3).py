import sys
sys.stdin = open('BOJ#15651_N&M(3).txt')

def perm(level, temp):
    if level == M:
        print(*temp)
        return
    for i in range(1, N+1):
        perm(level+1, temp+[i])

N, M = map(int, input().split())
perm(0, [])
