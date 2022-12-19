import sys
sys.stdin = open('BOJ#5247_Fire.txt')

from collections import deque

dcol = [-1,0,1,0]
drow = [0,1,0,-1]

def atime():
    for col in range(h):
        for row in range(w):
            if arr[col][row] == '@':
                global time
                queue = deque()
                queue.append((col, row))
                arr[col][row] = time

                time += 1
                for i in range(len(queue)):
                    col, row = queue.popleft()
                    for v in range(4):
                        ncol = col + dcol[v]
                        nrow = row + drow[v]
                        if 0<=ncol<h and 0<=nrow<w and arr[ncol][nrow] == '.':
                            arr[ncol][nrow] = time
                            queue.append((ncol, nrow))


w, h = map(int, input().split())    # w: 너비, h: 높이
arr = [list(input()) for _ in range(h)]
time = 0

atime()

for i in arr:
    print(*i)
