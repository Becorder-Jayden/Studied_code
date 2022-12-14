import sys
sys.stdin = open('BOJ#16236_BabyShark.txt')

from collections import deque

# target으로 가는 도중 큰 물고기는 돌아가야 함
# 왜 예제 3의 답이 12가 아니라 14지? -> 거리 계산을 잘못했기 때문

# 이동가능한 범위
dcol = [-1,0,1,0]
drow = [0,1,0,-1]

def hunt_fish():
    global time, arr, baby_idx, baby_shark
    time += target[0]       # 이동 후 시간 갱신
    arr[baby_idx[0]][baby_idx[1]] = 0   # 현재 위치 초기화
    ncol, nrow = target[1]
    arr[ncol][nrow] = 9     # 이동한 위치에 상어 표시

    baby_shark[1] += 1     # 상어 몸집 +1
    if baby_shark[0] == baby_shark[1]:
        baby_shark[0] += 1
        baby_shark[1] = 0

    baby_idx = (ncol, nrow)
    return

def find_target():
    global target, repeat
    visited = [[0] * N for _ in range(N)]
    visited[baby_idx[0]][baby_idx[1]] = -1      # 아기상어의 시작 위치

    # 먹을 수 있는 물고기가 공간에 있는지 조회
    eatable = []

    # 도달 할 수 있는 곳인지 확인
    queue = deque()
    queue.append((baby_idx[0], baby_idx[1]))
    dist = 0
    while queue:
        dist += 1
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0 <= ncol < N and 0 <= nrow < N and visited[ncol][nrow] == 0:
                    if arr[ncol][nrow] <= baby_shark[0]:
                        queue.append((ncol, nrow))
                        visited[ncol][nrow] = dist  # 이동가능한 공간
                    else:
                        visited[ncol][nrow] = 0  # 이동할수 없는 공간

    for col in range(N):
        for row in range(N):
            if 0 < arr[col][row] < baby_shark[0] and visited[col][row] > 0:
                eatable.append((visited[col][row], (col, row)))

    if not eatable:  # eatable이 없을 때
        target = []
        repeat = False
        return
    else:  # eatable이 존재할 때
        eatable.sort(key=lambda x: (x[0], x[1][0], x[1][1]))
        target = eatable[0]
        return


def move():
    find_target()

    # 목표가 있을 때, 사냥
    if target:
        hunt_fish()

N = int(input())    # 공간의 크기
arr = [list(map(int, input().split())) for _ in range(N)]   # 9: 아기 상어
baby_shark = [2, 0]
time = 0
repeat = True

# 아기상어 위치 찾기
for col in range(N):
    for row in range(N):
        if arr[col][row] == 9:
            baby_idx = (col, row)

while repeat:
    move()

print(time)








# try 1
# from collections import deque
#
# # target으로 가는 도중 큰 물고기는 돌아가야 함
# # 왜 예제 3의 답이 12가 아니라 14지? -> 거리 계산을 잘못했기 때문
#
# # 이동가능한 범위
# dcol = [-1,0,1,0]
# drow = [0,1,0,-1]
#
#
# def hunt_fish():
#     global time, arr, baby_idx, baby_shark
#     time += target[0]       # 이동 후 시간 갱신
#     arr[baby_idx[0]][baby_idx[1]] = 0   # 현재 위치 초기화
#     ncol, nrow = target[1]
#     arr[ncol][nrow] = 9     # 이동한 위치에 상어 표시
#
#
#     baby_shark[1] += 1     # 상어 몸집 +1
#     if baby_shark[0] == baby_shark[1]:
#         baby_shark[0] += 1
#         baby_shark[1] = 0
#
#     baby_idx = (ncol, nrow)
#     return
#
# def find_target():
#     global target, repeat
#     visited = [[0] * N for _ in range(N)]
#     visited[baby_idx[0]][baby_idx[1]] = 2
#
#     # 먹을 수 있는 물고기가 공간에 있는지 조회
#     eatable = []
#
#     # 도달 할 수 있는 곳인지 확인
#     queue = deque()
#     queue.append((baby_idx[0], baby_idx[1]))
#     while queue:
#         col, row = queue.pop()
#         for v in range(4):
#             ncol = col + dcol[v]
#             nrow = row + drow[v]
#             if 0 <= ncol < N and 0 <= nrow < N and visited[ncol][nrow] == 0:
#                 if arr[ncol][nrow] <= baby_shark[0]:
#                     queue.append((ncol, nrow))
#                     visited[ncol][nrow] = 1  # 이동가능한 공간
#                 else:
#                     visited[ncol][nrow] = -1  # 이동할수 없는 공간
#
#     for col in range(N):
#         for row in range(N):
#             if 0 < arr[col][row] < baby_shark[0] and visited[col][row] == 1:
#                 eatable.append((abs(baby_idx[0] - col) + abs(baby_idx[1] - row), (col, row)))
#     if not eatable:  # eatable이 없을 때
#         target = []
#         repeat = False
#         return
#     else:  # eatable이 존재할 때
#         eatable.sort(key=lambda x: (x[0], x[1][0], x[1][1]))
#         target = eatable[0]
#         return
#
#
# def move():
#     print('==== move 실행 ====')
#     # 목표 확인
#     find_target()
#     print('target:', target)
#
#     # 목표가 있을 때, 사냥
#     print('time:', time)
#     if target:
#         hunt_fish()
#     # else:
#     #     print('target이 없음')
#
#     for i in arr:
#         print(*i)
#
#
# N = int(input())    # 공간의 크기
# arr = [list(map(int, input().split())) for _ in range(N)]   # 9: 아기 상어
# baby_shark = [2, 0]
# time = 0
# repeat = True
#
# # 아기상어 위치 찾기
# for col in range(N):
#     for row in range(N):
#         if arr[col][row] == 9:
#             baby_idx = (col, row)
#
#
#
# print(baby_idx)
#
# while repeat:
#     move()
#
# print(time)
