import sys
sys.stdin = open('BOJ#2580_Sdoku.txt')

dcol = [1, -1, 0, 0]
drow = [0, 0, -1, 1]

def dfs(idx_lst):
    for col, row in idx_lst:
        for j in range(1, 10):
            arr[col][row] = j
            for v in range(4):
                d = 1
                while True:
                    ncol = col + dcol[v]*d
                    nrow = row + drow[v]*d
                    if 0<=ncol<9 and 0<=nrow<9:
                        if arr[ncol][nrow] != j:
                            d += 1
                        else:
                            continue
                    else:
                        break


arr = [list(map(int, input().split())) for _ in range(9)]
zero_li = []
for col in range(9):
    for row in range(9):
        if arr[col][row] == 0:
            zero_li.append((col, row))

dfs(zero_li)