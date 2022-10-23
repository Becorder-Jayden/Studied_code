import sys
sys.stdin = open('BOJ#2580_Sudoku.txt')

# 10/7 짜면 이대로 짜겠는데.. 백트래킹 적용은 어떻게 해?

# solution

# cnt_li로 확인, cnt_zero == 1일 때, 비어있는 숫자 입력
# 가로방향 탐색
def exp_col(col, row):
    cnt_li = [0]*10
    cnt_zero = 0

    for i in range(9):
        cnt_li[arr[col][i]] += 1

    for i in cnt_li:            # 0의 개수 확인
        if i == 0:
            cnt_zero += 1

    # 탐색했을 때 한 곳이 비어 있을 경우 바로 처리
    if cnt_zero == 1:
        for i in range(9):
            if arr[col][i] == 0:
                arr[col][i] = cnt_li.index(0)

    # 탐색했을 때 여러 곳이 비어 있을 경우
    elif cnt_zero > 1:
        print(cnt_zero)
        temp = []
        for i in range(9):
            if cnt_li[i] == 0:
                temp.append(i)
        print(temp)



# 새로방향 탐색
def exp_row(col, row):
    cnt_li = [0] * 10
    cnt_zero = 0

    for i in range(9):
        cnt_li[arr[i][row]] += 1

    for i in cnt_li:
        if i == 0:
            cnt_zero += 1
            if cnt_zero > 1:
                return

    if cnt_zero == 1:
        for i in range(9):
            if arr[i][row] == 0:
                arr[i][row] = cnt_li.index(0)

# 3x3 방향 탐색
def exp_3x3(col, row):
    cnt_li = [0] * 10
    cnt_zero = 0
    for c in range(3):
        for r in range(3):
            cnt_li[arr[col+c][row+r]] += 1

    for i in cnt_li:
        if i == 0:
            cnt_zero += 1
            if cnt_zero > 1:
                return

    if cnt_zero == 1:
        for c in range(3):
            for r in range(3):
                if arr[col+c][row+r] == 0:
                    arr[col+c][row+r] = cnt_li.index(0)


arr = [list(map(int, input().split())) for _ in range(9)]
zero_li = []
for col in range(9):
    for row in range(9):
        if arr[col][row] == 0:
            zero_li.append((col, row))

for i in range(9):
    exp_col(i, 0)
    exp_row(0, i)

for col in range(0, 9, 3):
    for row in range(0, 9, 3):
        exp_3x3(col, row)

for i in range(9):
    exp_col(i, 0)
    exp_row(0, i)

for col in range(0, 9, 3):
    for row in range(0, 9, 3):
        exp_3x3(col, row)

for i in arr:
    print(*i)


