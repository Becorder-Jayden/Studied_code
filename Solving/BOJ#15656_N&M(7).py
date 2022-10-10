import sys
sys.stdin = open('BOJ#15656_N&M(7).txt')

def perm(level, temp):
    if level == M:
        print(*temp)
        return

    for i in range(N):
        perm(level+1, temp+[arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [0] * N
perm(0, [])