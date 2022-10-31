import sys
sys.stdin = open('BOJ#14503_RobotCleaner.txt')

dcol = [0, 1, 0, -1]
drow = [-1, 0, 1, 0]

def clean(col, row, d):
    arr[col][row] = 2
    return turn_left(col, row, d)


def turn_left(col, row, d):
    for i in range(4):
        ncol = col + dcol[(d+i+3)%4]
        nrow = row + drow[(d+i+3)%4]
        if 0<=ncol<N and 0<=nrow<M:
            print(ncol, nrow)
            if arr[ncol][nrow] == 0:
                clean(ncol, nrow, (d+3)%4)


N, M = map(int, input().split())
r, c, d = map(int, input().split())     # r: 가로, c: 세로, d: 방향(0: 북, 1:동, 2:남, 3:서)
arr = [list(map(int, input().split())) for _ in range(N)]
arr[c][r] = 5       # 5: 청소기 위치 표시

turn_left(1, 1, 0)

for i in arr:
    print(i)

