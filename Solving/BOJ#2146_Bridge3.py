import sys
sys.stdin = open('BOJ#2146_Bridge.txt')

# 경계면을 기준으로 탐색
# 섬마다 표기를 다르게 하는 방법 도전
# visited 표기 생각해보기

from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]

def divide_island():
    cnt = 1
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:
                # arr[col][row] = cnt     # 현 위치 섬 표기
                queue = deque()         # queue 생성후 현재 위치 입력
                queue.append((col, row))
                cnt += 1
                while queue:
                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        arr[col][row] = cnt
                        for v in range(4):
                            ncol = col+dcol[v]
                            nrow = row+drow[v]
                            if 0<=ncol<N and 0<=nrow<N:
                                if arr[ncol][nrow] == 1:
                                    queue.append((ncol, nrow))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]


divide_island()

for i in arr:
    print(i)