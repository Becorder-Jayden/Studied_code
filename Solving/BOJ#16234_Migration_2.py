import sys
sys.stdin = open('BOJ#16234_Migration.txt')

# 상, 우, 하, 좌
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

from collections import deque

def grouping():
    visited = [[0]*N for _ in range(N)]
    group_cnt = 0

    for col in range(N):
        for row in range(N):
            if visited[col][row] == 0:
                queue = deque()
                queue.append((col, row))
                group[]
                visited[col][row] = 1
                while queue:
                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        for v in range(4):
                            ncol = col + dcol[v]
                            nrow = row + drow[v]
                            if 0<=ncol<N and 0<=nrow<N and visited[ncol][nrow] == 0:
                                visited[ncol][nrow] = 1





N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

