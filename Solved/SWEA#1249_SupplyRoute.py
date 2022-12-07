import sys
sys.stdin = open('SWEA#1249_SupplyRoute.txt')

from collections import deque

# 상, 우, 하, 좌
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def exp(col, row):
    queue = deque()
    queue.append((col, row))
    while queue:
        col, row = queue.popleft()
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0<=ncol<N and 0<=nrow<N:
                if visited[ncol][nrow] == 0:
                    visited[ncol][nrow] = 1
                    cost[ncol][nrow] = cost[col][row] + arr[ncol][nrow]
                    queue.append((ncol, nrow))
                else:
                    # 코드 수정 부분: 25번 코드 → 26~28번 코드
                    # if cost[ncol][nrow] > cost[col][row]+arr[ncol][nrow]:
                    #     queue.append((ncol, nrow))
                    # cost[ncol][nrow] = min(cost[ncol][nrow], cost[col][row]+arr[ncol][nrow])
                    if cost[ncol][nrow] > cost[col][row] + arr[ncol][nrow]:
                        cost[ncol][nrow] = cost[col][row] + arr[ncol][nrow]
                        queue.append((ncol, nrow))
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # slicing을 이용한 deepcopy: 1차원(arr[:]을 N열 만큼 복사해서 리스트로 만든다)
    cost = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    exp(0, 0)

    # # print()
    print(f'#{tc} {cost[N-1][N-1]}')
    # for i in cost:
    #     print(*i)
    # print()
    # for i in cost:
    #     print(*i)
    # print()
    # for i in visited:
    #     print(*i)

