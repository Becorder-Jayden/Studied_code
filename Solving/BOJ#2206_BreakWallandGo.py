import sys
sys.stdin = open('input.txt')

# bfs 탐색중인데 한 방향으로만 가고 있음 -> 체크 필요..

from collections import deque

dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

# (col, row)부터 (N, M)까지 이동, 경로의 길이?
def route(col, row):
    queue = deque()
    queue.append((col, row))
    visited[col-1][row-1] = 1
    cnt = 1

    while queue:
        cnt += 1
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if ncol == N-1 and nrow == M-1:
                    visited[ncol][nrow] = cnt
                    return visited[ncol][nrow]

                elif 0<=ncol<N and 0<=nrow<M and arr[ncol][nrow] == 0 and visited[ncol][nrow] == 0:
                    visited[ncol][nrow] = cnt
                    queue.append((ncol, nrow))



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
hammer = 1

visited = [[0] * M for n in range(N)]

route(6, 1)  # expect : 4
# print(route(6, 1))

# for i in arr:
#     print(*i)
#
# for i in visited:
#     print(i)
