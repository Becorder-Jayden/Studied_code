import sys
sys.stdin = open('BOJ#2580_Sudoku.txt')

# 10/7 짜면 이대로 짜겠는데.. 백트래킹 적용은 어떻게 해?

def exp_col(col, row):
    cnt_li = [0]*10
    cnt_zero = 0
    for i in range(9):
        cnt_li[arr[col][i]] += 1
    for i in cnt_li:
        if i == 0:
            cnt_zero += 1
    if cnt_zero == 1:
        for i in range(9):
            if arr[col][i] == 0:
                arr[col][i] = cnt_li.index(0)

def exp_row(col, row):
    cnt_li = [0] * 10
    cnt_zero = 0
    for i in range(9):
        cnt_li[arr[i][row]] += 1
    for i in cnt_li:
        if i == 0:
            cnt_zero += 1
    if cnt_zero == 1:
        for i in range(9):
            if arr[i][row] == 0:
                arr[i][row] = cnt_li.index(0)

def exp_3x3(col, row):
    pass


arr = [list(map(int, input().split())) for _ in range(9)]
zero_li = []
for col in range(9):
    for row in range(9):
        if arr[col][row] == 0:
            zero_li.append((col, row))

for col in range(9):
    exp_col(col, 0)

for row in range(9):
    exp_row(0, row)

for i in arr:
    print(i)

'''
[1, 3, 5, 4, 6, 9, 2, 7, 8]
[7, 8, 2, 1, 0, 5, 6, 0, 9]
[0, 6, 0, 2, 7, 8, 1, 3, 5]
[3, 2, 1, 5, 4, 6, 8, 9, 7]
[8, 0, 4, 9, 1, 3, 5, 0, 6]
[5, 9, 6, 8, 2, 7, 4, 1, 3]
[9, 1, 7, 6, 5, 2, 0, 8, 0]
[6, 0, 3, 7, 0, 1, 9, 5, 2]
[2, 5, 8, 3, 9, 4, 7, 6, 1]
'''

'''
[1, 3, 5, 4, 6, 9, 2, 7, 8]
[7, 8, 2, 1, 0, 5, 6, 0, 9]
[4, 6, 9, 2, 7, 8, 1, 3, 5]
[3, 2, 1, 5, 4, 6, 8, 9, 7]
[8, 0, 4, 9, 1, 3, 5, 0, 6]
[5, 9, 6, 8, 2, 7, 4, 1, 3]
[9, 1, 7, 6, 5, 2, 3, 8, 4]
[6, 0, 3, 7, 0, 1, 9, 5, 2]
[2, 5, 8, 3, 9, 4, 7, 6, 1]
'''
