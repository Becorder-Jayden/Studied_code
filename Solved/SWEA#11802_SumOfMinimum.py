import sys
sys.stdin = open('../Solving/input.txt')

# dcol = [1, 0]
# drow = [0, 1]
#
# def exp(col, row, S):
#     if (col, row) == (N-1, N-1):
#         S += arr[N-1][N-1]
#         ans_li.append(S)
#         return
#     for v in range(2):
#         ncol = col+dcol[v]
#         nrow = row+drow[v]
#         if 0<=ncol<N and 0<=nrow<N:
#             exp(ncol, nrow, S+arr[col][row])
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans_li = []
#
#     exp(0, 0, 0)
#     print(f'#{tc} {min(ans_li)}')


# 가지치기 시도

dcol = [1, 0]
drow = [0, 1]

def exp(col, row, S):
    global ans
    if ans < S:                         # 가지치기
        return
    if (col, row) == (N - 1, N - 1):
        S += arr[N - 1][N - 1]
        if ans > S:                     # 가지치기
            ans = S
        return
    for v in range(2):
        ncol = col + dcol[v]
        nrow = row + drow[v]
        if 0 <= ncol < N and 0 <= nrow < N:
            exp(ncol, nrow, S + arr[col][row])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999

    exp(0, 0, 0)
    print(f'#{tc} {ans}')