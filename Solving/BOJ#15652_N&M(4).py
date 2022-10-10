import sys
sys.stdin = open('BOJ#15652_N&M(4).txt')

def dfs(level, start, temp):
    if level == M:
        print(*temp)
        return
    for i in range(start, N+1):
        dfs(level+1, i, temp+[i])

N, M = map(int, input().split())
dfs(0, 1, [])