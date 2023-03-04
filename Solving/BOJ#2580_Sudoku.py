import sys
sys.stdin = open('BOJ#2580_Sudoku.txt')


def ck_row(col, n):
    for i in range(9):
        if arr[col][i] == n:
            return False
    return True

def ck_col(n, row):
    for i in range(9):
        if arr[i][row] == n:
            return False
    return True

def ck_3x3(col, row, n):
    ncol = col//3 * 3   #?
    nrow = row//3 * 3   #?
    for c in range(3):
        for r in range(3):
            if n == arr[ncol+c][nrow+r]:
                return False
    return True


def exp(n):
    if n == len(zeros):
        return True
    col, row = zeros[n]

    for n
    return






arr = [list(map(int, input().split())) for _ in range(9)]

for i in arr:
    print(*i)

zeros = []
for col in range(9):
    for row in range(9):
        if arr[col][row] == 0:
            zeros.append((col, row))

for col, row in zeros:
    exp(col, row)