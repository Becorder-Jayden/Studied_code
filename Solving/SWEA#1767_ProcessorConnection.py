import sys
sys.stdin = open('SWEA#1767_ProcessorConnection.txt')

# 소나서포터(알고리즘 마스터)조언 : 블럭으로 함수를 만들어 나가야 함. 큰 블럭부터(작은 블럭이 있다고 고려하고)


dcol = [1, -1, 0, 0, 0]
drow = [0, 0, 1, -1, 0]

# 메인 재귀여서 주 함수로 치고 생각하자.
def subset(level, lst, temp):
    if level == len(lst):
        return

    print(temp)
    #exp(temp)
    col, row = lst[level]
    #for col, row in lst:
    for v in range(5):
        if v == 4:
            subset(level+1, lst, temp)
        else:
            arr[col][row] = 3
            dfs(col, row, v)
            arr[col][row] = 1
            subset(level+1, lst, temp+[lst[level]])
            arr[col][row] = 3
            reset(col, row, v, d-1)
            arr[col][row] = 1

    # subset(level+1, lst, temp)
    # subset(level+1, lst, temp+[lst[level]])

# dfs return 약간 이상해 v
# 들어갈 함수를 어떻게 설정할지 잘 모르겠다.
# def dfs(col, row, v):
#     if col == 0 or row == 0 or col == N or row == N:
#             ###
#         return
#     ncol = col + dcol[v]
#     nrow = row + drow[v]
#     if ncol == col and nrow == row:
#         return
#     arr[ncol][nrow] = True
#     if 0<=ncol<N-1 and 0<=nrow<N-1:
#         dfs(ncol, nrow, v)
#     #     # arr[ncol][nrow] = 0
#     # arr[ncol][nrow] = 0

def dfs(col, row, v):
    global d
    d = 0
    while True:
        d += 1
        ncol = col + dcol[v] * d
        nrow = row + drow[v] * d
        if 0 <= ncol < N and 0 <= nrow <N and arr[ncol][nrow] == 0:
            arr[ncol][nrow] = 4
        else: break

def reset(col, row, v, dist):
    # d = 0
    for i in range(dist):
        d += 1
        ncol = col + dcol[v] * d
        nrow = row + drow[v] * d
        if 0 <= ncol < N and 0 <= nrow < N and arr[ncol][nrow] == 4:
            arr[ncol][nrow] = 0
        else: break

def exp(lst):
    for col, row in lst:
        for v in range(5):
            dfs(col, row, v)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pc_lst = []

    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1 and not (col == 0 or row == 0):
                pc_lst.append((col, row))

    print(pc_lst)
    subset(0, pc_lst, [])

    #exp(pc_lst)



    for i in arr:
        print(i)