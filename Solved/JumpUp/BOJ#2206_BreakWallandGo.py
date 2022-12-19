import sys
sys.stdin = open('BOJ#2206_BreakWallandGo.txt')

# 모든 벽을 부셔서 최단 거리를 구해보는 알고리즘으로 풀 수 없다? https://www.acmicpc.net/board/view/84960
# → 시간 : BFS 기본 시간 * 부술 수 있는 벽의 수 : 문제에서 1000*1000으로 시간제한에 걸린다

# 구글링 : 3차원 풀이 방식 사용
# 벽을 단 한번만 부술수 있기 때문에 벽을 부쉈는지의 여부를 하나의 차원에 나타내서 풀 수 있다

# 3차원방식 도입 풀이
from collections import deque

dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def find_route():
    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        col, row, bkw = queue.popleft()     # bkw: 벽을 부순 횟수
        if col == N-1 and row == M-1:       # 목표지점에 도달했을 경우
            return visited[col][row][bkw]   # 이동 거리를 반환

        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0<=ncol<N and 0<=nrow<M:     # arr 범위 내에서
                if arr[ncol][nrow] == 1 and bkw == 0:   # 탐색한 곳이 벽이고, 벽을 부순적이 없을 때
                    # 탐색한 곳으로 진행, 벽을 부슨 상태를 가정했기 때문에 [ncol][nrow][1](벽을 부쉈을 때)에 기록
                    # 현재까지 이동한 거리에서 +1
                    visited[ncol][nrow][1] = visited[col][row][0] + 1
                    queue.append((ncol, nrow, 1))

                elif arr[ncol][nrow] == 0 and visited[ncol][nrow][bkw] == 0:    # 탐색한 곳이 빈 공간,
                    # 현재까지 이동한 거리 +1
                    visited[ncol][nrow][bkw] = visited[col][row][bkw] + 1
                    queue.append((ncol, nrow, bkw))

    # 중간에 return 되지 않았을 경우(arr[N-1][M-1]에 도달하지 못함) : -1을 반환
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
wall_lst = []

# 3차원 행렬 만들기 - visited[x][y][0]: 벽을 뚫지 않았을 때, visited[x][y][1]: 벽을 뚫었을 때
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(find_route())

for i in arr:
    print(*i)
print()
for i in visited:
    print(*i)




# 시간초과 & 메모리 초과
# from collections import deque
#
# dcol = [-1, 0, 1, 0]
# drow = [0, 1, 0, -1]
#
# def find_route():
#     queue = deque()
#     queue.append((0, 0))
#     dist = 0
#     while queue:
#         dist += 1
#         for i in range(len(queue)):
#             col, row = queue.popleft()
#             # arr_copy[col][row] = dist       # dist: 지나온 거리      # 메모리 초과 발생
#             for v in range(4):
#                 ncol = col + dcol[v]
#                 nrow = row + drow[v]
#                 if 0<=ncol<N and 0<=nrow<M and arr_copy[ncol][nrow] == 0:    # 주어진 범위 내에서 벽/지나온 곳이 아닐 경우
#                     arr_copy[ncol][nrow] = dist       # 메모리 초과 해결(?)
#                     queue.append((ncol, nrow))
#
#     # print()
#     # for i in arr_copy:
#     #     print(*i)
#
# N, M = map(int, input().split())
# arr_orgin = [list(map(int, input())) for _ in range(N)]
# wall_lst = []
# answer = 0xffff
#
# # 벽이 위치한 인덱스 파악
# for col in range(N):
#     for row in range(M):
#         if arr_orgin[col][row] == 1:
#             wall_lst.append((col, row))
#
# # 각 벽이 부셔진 상태로 진행했을 때 결과 확인
# for col, row in wall_lst:
#     arr_copy = [arr_orgin[i][:] for i in range(N)]
#     arr_copy[col][row] = 0
#     find_route()
#     arr_copy[col][row] = 1
#
#     if arr_copy[N-1][M-1]:   # 목적지 도달 여부 판단
#         answer = min(arr_copy[N-1][M-1], answer)
#
# # 정답 출력
# if answer == 0xffff:
#     print(-1)
# else:
#     print(answer+1)