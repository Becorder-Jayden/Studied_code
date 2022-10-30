import sys
sys.stdin = open('BOJ#14503_RobotCleaner.txt')


# 1. 현재 위치를 청소
# def clean(col, row, v):
#     if arr[col][row] == 0:
#         arr[col][row] = 2


# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 탐색 진행
def exp(col, row, v):
    if v == 0:      # 북쪽을 보고 있는 경우 탐색
        if arr[col][row-1] == 0:
            arr[col][row] = 2       # 머물던(청소한) 자리
            arr[col][row-1] = 5     # 이동한 자리
            for vec in range(4):
                exp(col, row-1, (3-vec)%4)
        else:
            return
    elif v == 3:    # 서쪽을 보고 있는 경우
        if arr[col+1][row] == 0:
            arr[col][row] = 2
            arr[col+1][row] = 5
            for vec in range(4):
                exp(col+1, row, (2-vec)%4)
        else:
            return
    elif v == 2:    # 남쪽을 보고 있는 경우
        if arr[col][row+1] == 0:
            arr[col][row] = 2
            arr[col][row+1] = 5
            for vec in range(4):
                exp(col, row+1, (1-vec)%4)
        else:
            return
    elif v == 1:
        if arr[col-1][row] == 0:
            arr[col][row] = 2
            arr[col-1][row] = 5
            for vec in range(4):
                exp(col-1, row, (0-vec)%4)
        else:
            return


    print(col, row, v)




# 청소기의 움직임
def start(col, row, v):

    # 1. 청소
    if arr[col][row] == 0:
        arr[col][row] = 2   # 2: 청소기가 지나간 자리

    # 2. 탐색
    exp(col, row, v)


N, M = map(int, input().split())
r, c, d = map(int, input().split())     # r: 가로, c: 세로, d: 방향(0: 북, 1:동, 2:남, 3:서)
arr = [list(map(int, input().split())) for _ in range(N)]
arr[c][r] = 5       # 5: 청소기 위치 표시


print(N, M)
print(r, c, d)
for i in arr:
    print(i)
start(c, r, d)

