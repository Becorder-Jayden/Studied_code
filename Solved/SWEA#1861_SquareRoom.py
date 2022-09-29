import sys
sys.stdin = open('../Solving/input.txt')

# 9/16 풀이 완료

dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

def dfs(col, row):
    global cnt
    for v in range(4):
        ncol = col + dcol[v]
        nrow = row + drow[v]
        if 0<=ncol<N and 0<=nrow<N:
            if arr[ncol][nrow] == arr[col][row]+1:
                dfs(ncol, nrow)
                cnt += 1
    return cnt

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    li = []
    for col in range(N):
        for row in range(N):
            cnt = 1
            li.append((arr[col][row], dfs(col, row)))

    li = sorted(li, key=lambda x : (-x[1], x[0]))
    print(f'#{t+1}', li[0][0], li[0][1])