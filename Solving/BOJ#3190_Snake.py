import sys
sys.stdin = open('BOJ#3190_Snake.txt')

from collections import deque

# U, R, D, L
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def move():
    global arr, head
    col, row, vec = head
    ncol = col + dcol[vec]
    nrow = row + drow[vec]

    if 0<=ncol<N and 0<=nrow<N:
        if arr[ncol][nrow] == 5:    # 사과를 먹었을 때
            arr[ncol][nrow] = 1     # 머리 위치가 바뀌고
            snake.append([ncol, nrow, vec])     # 뱀의 몸 길이 추가

        elif arr[ncol][nrow] == 0:  # 사과를 먹지 않았을 때
            arr[ncol][nrow] = 1     # 머리 위치가 바뀌고
            snake.append([ncol, nrow, vec])     # 뱀의 몸 길이 추가
            tcol, trow, vec = snake.popleft()   # 뱀의 몸 삭제
            arr[tcol][trow] = 0

        head = (ncol, nrow, vec)    # 머리 위치 업데이트
        return

    else: print('범위를 초과')
        


N = int(input())    # 보드의 크기
arr = [[0]*N for _ in range(N)]
arr[0][0] = 1   # 초기 뱀의 위치와 방향
snake = deque()
snake.append([0, 0, 1])
head = (0, 0, 1)
time = 0

K = int(input())    # 사과의 개수
for k in range(K):  # 사과의 위치 정보
    c, r = map(int, input().split())
    arr[c][r] = 5

turn = deque()
L = int(input())    # 방향 전환의 수
for l in range(L):  # 방향 전환 정보
    X, C = input().split()  # X: 실행 시점, C: 방향 (L: 왼쪽, D: 오른쪽)
    turn.append((int(X), C))

standby = turn.popleft()

while time != standby[0]:
    move()
    time += 1

if standby[1] == 'D':   # 오른쪽
    col, row, vec = snake.pop()
    vec = (vec+1)%4
    snake.append((col, row, vec))
# elif standby[1] == 'L':   # 왼쪽 방향전환

print('time:', time, 'standby:', standby)
for i in arr:
    print(*i)
































# # 게임 종료: 벽 또는 자신의 몸과 부딪힐 때
# 
# from collections import deque
# 
# # U, R, D, L
# dcol = [-1, 0, 1, 0]
# drow = [0, 1, 0, -1]
# 
# def go():   # 1초마다 뱀의 전진
#     global head, time
#     time += 1
#     col, row = head[0], head[1]
#     ncol = col + dcol[arr[head[0]][head[1]]]
#     nrow = row + drow[arr[head[0]][head[1]]]
#     if 0<=ncol<N and 0<=nrow<N and arr[ncol][nrow] == 0:
#         arr[ncol][nrow] = arr[col][row]
#         arr[col][row] = 0
#         head = (ncol, nrow)
# 
#     if time == turn[0][0]:
#         print(turn[0][0], 'turn 할 시간이야!')
#         turn.popleft()
# 
# N = int(input())    # 보드의 크기
# arr = [[0]*N for _ in range(N)]
# arr[0][0] = 1   # 초기 뱀의 위치와 방향
# head = (0, 0)
# time = 0
# 
# K = int(input())    # 사과의 개수
# for k in range(K):  # 사과의 위치 정보
#     c, r = map(int, input().split())
#     arr[c][r] = 4
# 
# turn = deque()
# L = int(input())    # 방향 전환의 수
# for l in range(L):  # 방향 전환 정보
#     X, C = input().split()  # X: 실행 시점, C: 방향 (L: 왼쪽, D: 오른쪽)
#     turn.append((int(X), C))
# print('turn:', turn)
# 
# while time <= 10:
#     go()
# 
# for i in arr:
#     print(*i)
# print(turn)