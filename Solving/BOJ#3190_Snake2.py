import sys
sys.stdin = open('BOJ#3190_Snake.txt')

# 덱 구조를 이용하면 편할 것 같다 : 뱀이 지나간 자리 표시, 뱀의 방향 전환
#   사과를 먹지 않으면 : 머리 이동, 꼬리 이동
#   사과를 먹었다면 : 머리 이동, 꼬리 이동x (길어졌기 때문에)
# go 함수를 만들어서 사용

from collections import deque

#상,우,하,좌
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def go():
    global now_col, now_row, now_vec, snake, time, standby
    # time += 1
    # turn이 존재할 때 popleft 이후 사용
    if standby and time == standby[0]:
        if turn:
            if time == standby[0]:
                if standby[1] == 'L':
                    now_vec = (now_vec-1)%4
                elif standby[1] == 'D':
                    now_vec = (now_vec+1)%4
                standby = False
    elif standby == False and turn:
        standby = turn.popleft()
    # else:
    ncol = now_col + dcol[now_vec]
    nrow = now_row + drow[now_vec]
    if 0<=ncol<N and 0<=nrow<N:
        if arr[ncol][nrow] == 0:    # 사과를 먹지 않았을 때
            snake.append((ncol, nrow, now_vec))     # 머리가 한 칸 이동
            tc, tr, tv = snake.popleft()    # 꼬리 하나를 떼어냄
            arr[tc][tr] = 0     # 꼬리었던 곳 초기화
            for c, r, v in snake:   # 뱀 정보 arr에 표기
                arr[c][r] = 1
            now_col, now_row, now_vec = ncol, nrow, now_vec

        elif arr[ncol][nrow] == 4:  # 사과를 먹을 때
            snake.append((ncol, nrow, now_vec))     # 머리가 한 칸 이동
            # 꼬리를 떼어내지 않음
            for c, r, v in snake:   #  뱀 정보 arr에 표기
                arr[c][r] = 1
            now_col, now_row, now_vec = ncol, nrow, now_vec

    time += 1

snake = deque()
turn = deque()

N = int(input())    # 보드의 크기
arr = [[0] * N for _ in range(N)]   # NxN 보드

K = int(input())    # 사과의 개수
for k in range(K):  # 사과의 위치 표시
    col, row = map(int, input().split())
    arr[col][row] = 4

L = int(input())    # 뱀의 방향 변환 횟수
for l in range(L):  # 뱀이 방향을 돌린 시점 표시
    X, C = input().split()      # X초에 회전(왼쪽/오른쪽)
    turn.append((int(X), C))

time = 0
now_col, now_row, now_vec = 0, 0, 1
arr[0][0] = 1
snake.append((0, 0, 0))
standby = False
print(standby)



print(time+1)
for i in arr:
    print(*i)