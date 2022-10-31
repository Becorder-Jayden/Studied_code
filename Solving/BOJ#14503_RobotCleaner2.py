import sys
sys.stdin = open('BOJ#14503_RobotCleaner.txt')

# 서, 남, 동, 북
dcol = [0, 1, 0, -1]
drow = [-1, 0, 1, 0]


def clean(col, row, d):
    if 0<=col<N and 0<=row<M:
        arr[col][row] = 2
        exp(col, row, d)


# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 탐색 진행
def exp(col, row, d):
    for i in range(4):
        ncol = col + dcol[(4+i-d)%4]
        nrow = row + drow[(4+i-d)%4]
        if 0<=nrow<N and 0<=nrow<M:
            if arr[ncol][nrow] == 0:
                clean(ncol, nrow, (5+i-d)%4)
            else:
                pass
    print('여기 도달?')






# 청소기의 움직임
# def start(col, row, d):


N, M = map(int, input().split())
r, c, d = map(int, input().split())     # r: 가로, c: 세로, d: 방향(0: 북, 1:동, 2:남, 3:서)
arr = [list(map(int, input().split())) for _ in range(N)]
arr[c][r] = 5       # 5: 청소기 위치 표시


print(N, M)
print(r, c, d)
exp(c, r, 1)
for i in arr:
    print(i)

