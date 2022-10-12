import sys
sys.stdin = open('BOJ#1799_Bishop.txt')

dcol = [-1, 1, 1, -1]
drow = [1, 1, -1, -1]


N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
for col in range(N):
    for row in range(N):
        if chess[col][row] == 1:
            dfs(col, row)