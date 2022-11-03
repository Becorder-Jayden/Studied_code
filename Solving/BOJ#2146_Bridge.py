import sys
sys.stdin = open('BOJ#2146_Bridge.txt')

from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
exp_lst = []

def exp(col, row):
    cnt = 1
    q = deque()
    q.append((col, row))

    while q:
        for i in range(len(q)):
            cnt += 1
            col, row = q.popleft()
            for v in range(4):
                ncol = col+dcol[v]
                nrow = row+drow[v]
                if 0<=ncol<N and 0<=nrow<N:
                    if arr[ncol][nrow] == 0:
                        arr[ncol][nrow] = cnt
                        q.append([ncol, nrow])
                    elif arr[ncol][nrow] == -1:
                        print(ncol, nrow, arr[ncol][nrow])


for col in range(N):
    for row in range(N):
        if arr[col][row] == 1:
            for v in range(4):
                ncol = col+dcol[v]
                nrow = row+drow[v]
                if 0<=ncol<N and 0<=nrow<N:
                    if arr[ncol][nrow] == 0:
                        arr[col][row] = -1     # 섬의 경계면
                        exp_lst.append((col, row))

# print(exp_lst)

# for test (0, 3)
# exp(0, 3)

for i in arr:
    print(i)