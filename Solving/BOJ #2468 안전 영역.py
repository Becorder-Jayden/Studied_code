import sys
sys.stdin = open('BOJ 2468.txt')

from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def bfs(col,row):
    queue = deque()
    queue.append((col, row))
    tf[col][row] = 0
    while queue:
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0<=ncol<N and 0<=nrow<N and tf[ncol][nrow] != 0:
                    queue.append((ncol, nrow))
                    tf[ncol][nrow] = 0

N = int(input())
arr = [list(map(int, input().split())) for n in range(N)]

find_li = []
for i in arr:
    for j in i:
        find_li.append(j)
highest = max(find_li)

answer_li = []
for height in range(0, highest+1):
    tf = [[1]*N for n in range(N)]
    for col in range(N):
        for row in range(N):
            if arr[col][row] <= height:
                tf[col][row] = 0

    cnt = 0
    for col in range(N):
        for row in range(N):
            if tf[col][row] != 0:
                bfs(col, row)
                cnt += 1
    answer_li.append(cnt)

print(max(answer_li))