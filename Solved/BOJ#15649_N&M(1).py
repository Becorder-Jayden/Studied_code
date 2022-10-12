import sys
sys.stdin = open('BOJ#15649_N&M(1).txt')

def dfs(level, temp):
    if level == M:
        print(*temp)
        return

    for i in range(1, N+1):
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(level+1, temp+[i])
        visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N+1)
dfs(0, [])
