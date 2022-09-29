import sys
sys.stdin = open('SWEA#5250.MinCost.py')

# 최적 경로 이동 → 최소한의 연료 사용
# 다익스트라부터 접근 실패
# 큐 사용 시도

from collections import deque

dcol = [0, 0, -1, 1]
drow = [1, -1, 0, 0]

def bfs(col, row):
    queue = deque()
    queue.append((col, row))

    while queue:
        col, row = queue.popleft()
        for v in range(4):
            ncol = col+dcol[v]
            nrow = row+drow[v]
            if 0<=ncol<N and 0<=nrow<N:                             # 일반적인 경로
                temp = 1 + D[col][row]

                if arr[ncol][nrow] > arr[col][row]:                 # 언덕위로 올라갈 때
                    temp += arr[ncol][nrow] - arr[col][row]

                if temp < D[ncol][nrow]:                            # 간선완화
                    D[ncol][nrow] = temp
                    queue.append((ncol, nrow))


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff]*N for _ in range(N)]                                 # 간선 비용 무한으로 설정
    D[0][0] = 0                                                         # 시작점 방문거리 0으로 만들기
    bfs(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')

