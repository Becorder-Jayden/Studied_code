import sys
sys.stdin = open('BOJ#2580_Sudoku.txt')

# 가로 방향 탐색
def exp_col(col):
    cnt_li = [0] * 10
    for r in range(9):
        cnt_li[arr[col][r]] += 1
    if cnt_li[0]:
        temp = []
        for i in range(1, 10):
            if cnt_li[i] == 0:
                temp.append(i)

        row_missing[col] = temp
        # print('col:', col, temp)

# 세로 방향 탐색
def exp_row(row):
    cnt_li = [0] * 10
    for c in range(9):
        cnt_li[arr[c][row]] += 1
    if cnt_li[0]:
        temp = []
        for i in range(1, 10):
            if cnt_li[i] == 0:
                temp.append(i)

        col_missing[row] = temp
        # print('row:', row, temp)


arr = [list(map(int, input().split())) for _ in range(9)]
col_missing = [0]*10
row_missing = [0]*10

for col in range(9):
    exp_col(col)

for row in range(9):
    exp_row(row)

print('cm:', col_missing)
print('rm:', row_missing)

for cm in col_missing:
    for i in cm:
        if