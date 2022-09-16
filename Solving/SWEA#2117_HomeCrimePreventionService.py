import sys
sys.stdin = open('input.txt')

## 9/16 못 품..

from collections import deque

dcol = [-1, 0, 1, 0]
drow = [0, -1, 0, 1]

def cost(k):
    return k**2 + (k-1)**2

def bfs(col, row):
    queue = deque()
    cnt = 1
    visited[col][row] = cnt
    queue.append((col, row))
    while queue:
        cnt += 1
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col+dcol[v]
                nrow = row+drow[v]
                if 0<=ncol<N and 0<=nrow<N and visited[ncol][nrow]==0:
                    visited[ncol][nrow] = cnt
                    queue.append((ncol, nrow))

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    bfs(0, 0)

    for i in visited:
        print(i)