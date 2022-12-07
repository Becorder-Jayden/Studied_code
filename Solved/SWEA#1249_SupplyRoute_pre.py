import sys
sys.stdin = open('../Solved/SWEA#1249_SupplyRoute.txt`')

## 9/30 두 방법에 대해 이해하고 정리, 후에 파일 이동시킬 것

# 최단 경로 → 다익스트라 적용, 교수님, 우선순위 큐 필요
from heapq import heappop, heappush

dcol = [0, 0, -1, 1]
drow = [-1, 1, 0, 0]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    D = [[0xfffff] * N for _ in range(N)]
    D[0][0] = 0

    # 우선순위 큐
    queue = []
    heappush(queue, (0, 0, 0))          # (거리, col, row)
    visit = [[0] * N for _ in range(N)]
    while queue:
        d, col, row = heappop(queue)
        if visit[col][row]:
            continue
        visit[col][row] = 1
        if col == N-1 and row == N-1:
            break
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0 <= ncol < N and 0<= nrow < N and D[ncol][nrow] > D[col][row] + arr[ncol][nrow]:
                D[ncol][nrow] = D[col][row] + arr[ncol][nrow]
                heappush(queue, (D[ncol][nrow], ncol, nrow))

    print(f'#{tc} {D[N-1][N-1]}')



# # BFS 풀이
# from collections import deque
#
# dcol = [0, 0, -1, 1]
# drow = [-1, 1, 0, 0]
#
# def bfs(col, row):
#     queue = deque()
#     queue.append((col, row))
#     while queue:
#         col, row = queue.popleft()
#         for v in range(4):
#             ncol = col + dcol[v]
#             nrow = row + drow[v]
#             if 0 <= ncol < N and 0 <= nrow < N and D[ncol][nrow] > D[col][row] + arr[ncol][nrow]:       # 간선최적화(?)
#                 D[ncol][nrow] = D[col][row] + arr[ncol][nrow]
#                 queue.append((ncol, nrow))
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     D = [[0xfffff] * N for _ in range(N)]                   # 연결 리스트를 만듬
#     D[0][0] = 0                                             # 자기 자신으로 가는 비용은 0
#     bfs(0, 0)
#     print(f'#{tc} {D[N-1][N-1]}')
