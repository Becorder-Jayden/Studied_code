import sys
sys.stdin = open('BOJ#2638_Cheeze.txt')

from collections import deque

dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def find_surface():     # 치즈의 표면을 찾기
    queue = deque()
    visited[0][0] = 1       # (0, 0)에서부터 탐색 시작
    queue.append((0, 0))
    while queue:
        col, row = queue.popleft()
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0<=ncol<N and 0<=nrow<M and visited[ncol][nrow] == 0 and arr[ncol][nrow] == 0:   # 치즈가 아닌 곳일 때
                visited[ncol][nrow] = 1     # 방문처리 후 너비우선탐색 진행
                queue.append((ncol, nrow))

def find_melt():    # 치즈가 녹을 곳 탐색 : 2곳 이상 공기와 접촉할 때
    global visited
    visited = [[0] * M for _ in range(N)]       # visited 초기화
    find_surface()      # 치즈의 표면을 탐색

    going_melt = []     # 녹을 예정인 곳을 리스트에 저장
    for col in range(N):
        for row in range(M):
            if visited[col][row] == 0:
                check = 0
                for v in range(4):
                    ncol = col + dcol[v]
                    nrow = row + drow[v]
                    if 0<=ncol<N and 0<=nrow<M and visited[ncol][nrow] == 1 and arr[ncol][nrow] == 0:
                        check += 1
                if check >= 2:
                    going_melt.append((col, row))

    return going_melt

def melt():     # 치즈가 녹는 것
    for c, r in find_melt():
        arr[c][r] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0

while find_melt():
    time += 1
    find_melt()
    melt()

print(time)



# 문제 잘못 이해 : 치즈 내부에 있는 공간 고려 x
# def check():
#     going_melt = []
#     for col in range(N):
#         for row in range(M):
#             if arr[col][row]:   # arr[col][row] == 1일 때
#                 checker = 0
#                 for v in range(4):
#                     ncol = col + dcol[v]
#                     nrow = row + drow[v]
#                     if 0<=ncol<M and 0<=nrow<M and arr[ncol][nrow] == 0:
#                         checker += 1
#                 if checker >= 2:
#                     going_melt.append((col, row))
#
#     return going_melt
#
# def melt():
#     global time
#     time += 1
#     for col, row in check():
#         arr[col][row] = 0
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# time = 0
#
#
# while check():
#     melt()
#
# print(time)