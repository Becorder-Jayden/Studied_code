import sys
sys.stdin = open('BOJ#14503_RobotCleaner.txt')

# 22/11/03 풀이 완료
# 배열 탐색의 경우 범위에 대해서 항상 신경쓸 것
# 디버깅을 위한 체크 방식을 고려해둘 것


dcol = [0, 1, 0, -1]
drow = [-1, 0, 1, 0]

def check(col, row, dir):   # dir: 바라보는 방향
    if dir == 0:
        if 0<=col-1 and arr[col-1][row] == 0:
            exp(col-1, row, dir)
    elif dir == 3:
        if 0<=row-1 and arr[col][row-1] == 0:
            exp(col, row-1, dir)
    elif dir == 2:
        if col+1<N and arr[col+1][row] == 0:
            exp(col+1, row, dir)
    elif dir == 1:
        if row+1<M and arr[col][row+1] == 0:
            exp(col, row+1, dir)

def exp_except(col, row, dir):
    if col+1<N and dir == 0 and arr[col+1][row] != 1:
        exp(col+1, row, dir)
    elif row+1<M and dir == 3 and arr[col][row+1] != 1:
        exp(col, row+1, dir)
    elif 0<=col-1 and dir == 2 and arr[col-1][row] != 1:
        exp(col-1, row, dir)
    elif 0<=row-1 and dir == 1 and arr[col][row-1] != 1:
        exp(col, row-1, dir)

def exp(col, row, dir):
    global answer, cnt

    if arr[col][row] == 0:
        answer += 1
        cnt += 1
        arr[col][row] = cnt

    # 4방향 탐색
    for i in range(4):
        check(col, row, (dir-1-i)%4)

    # 네방향 모두 청소가 되어있거나 벽인 경우
    exp_except(col, row, dir)

    # 위 과정이 모두 통과했을때 정답을 출력하고 종료
    print(answer)
    exit()


N, M = map(int, input().split())
r, c, d = map(int, input().split())     # r: 가로, c: 세로, d: 방향(0: 북, 1:동, 2:남, 3:서)
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
answer = 0

exp(r, c, d)

