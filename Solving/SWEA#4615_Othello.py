import sys
sys.stdin = open('SWEA#4012_Cook.txt')

## 9/16 집에가서 다시 풀어보기 ㅠㅠ


# 8방향: U, UR, R, RD, D, DL, L, LU
dcol = [1, 1, 0, -1, -1, -1, 0, 1]
drow = [0, 1, 1, 1, 0, -1, -1, -1]

# def dfs(col, row, color, v):
#     global li
#     ncol = col + dcol[v]
#     nrow = row + drow[v]
#     if 0<=ncol<N and 0<=nrow<N and arr[ncol][nrow]:
#         if arr[ncol][nrow] == color:
#             return arr[col][row]
#         else:
#             a = dfs(ncol, nrow, color, v)
#             li.append(a)
#
def play(r, c, color):
    li = []
    col, row = c-1, r-1
    arr[col][row] = color
    for v in range(8):
        ncol = col + dcol[v]
        nrow = row + drow[v]
        while 0<=ncol<N and 0<=nrow<N and arr[ncol][nrow] and arr[ncol][nrow] != color:
            ncol += dcol[v]
            nrow += drow[v]
        print(ncol, nrow, arr[ncol-1][nrow-1])



T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    # 게임 세팅
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = arr[N//2-1][N//2-1] = 2

    # 게임 시작
    for m in range(M):
        r, c, color = map(int, input().split())
        play(r, c, color)

        for i in arr:
            print(i)
        print()