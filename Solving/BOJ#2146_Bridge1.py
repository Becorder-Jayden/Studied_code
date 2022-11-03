import sys
sys.stdin = open('BOJ#2146_Bridge.txt')


# 경계면을 기준으로 탐색
# 섬마다 표기를 다르게 하는 방법 도전
# visited 표기 생각해보기

from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [arr[i][:] for i in range(len(arr))]

border_lst = []
answer_lst = []

# 섬 구분
def divide_island():
    cnt = 0
    for col in range(N):
        for row in range(N):
            if visited[col][row] == 1:
                cnt -= 1
                queue = deque()
                queue.append((col, row))
                while queue:
                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        visited[col][row] = cnt
                        for v in range(4):
                            ncol = col+dcol[v]
                            nrow = row+drow[v]
                            if 0<=ncol<N and 0<=nrow<N and visited[ncol][nrow] == 1:
                                visited[col][row] = cnt
                                queue.append((ncol, nrow))

# 섬의 경계면 -1로 표시
def find_border():
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:  # 1의 값을 갖는 지점 중에서
                for v in range(4):
                    ncol = col+dcol[v]
                    nrow = row+drow[v]
                    if 0<=ncol<N and 0<=nrow<N:
                        if arr[ncol][nrow] == 0:        # 주변값으로 0을 갖는 곳
                            arr[col][row] = -1          # 섬의 경계면 표시

            # 경계로 표시된 곳의 인덱스를 border_lst에 담음
            if arr[col][row] == -1:
                border_lst.append((col, row))

# find_border()
divide_island()

for i in arr:
    print(i)

queue = deque()
queue.extend(border_lst)
cnt = 0
while queue:
    cnt += 1
    for i in range(len(queue)):
        col, row = queue.popleft()
        for v in range(4):
            ncol = col+dcol[v]
            nrow = row+drow[v]
            if 0<=ncol<N and 0<=nrow<N:
                if arr[ncol][nrow] == 0 and visited[ncol][nrow] == 0:
                    arr[ncol][nrow] = cnt
                    visited[ncol][nrow] = visited[col][row]
                    queue.append((ncol, nrow))
                elif arr[col][row] and arr[ncol][nrow] and visited[col][row] and visited[ncol][nrow] and visited[col][row] != visited[ncol][nrow]:
                    if arr[col][row] > 0 and arr[ncol][nrow] > 0:
                        if arr[col][row] < 0:
                            answer_lst.append(arr[ncol][nrow])
                        elif arr[ncol][nrow] < 0:
                            answer_lst.append(arr[col][row])
                        else:
                            answer_lst.append(arr[col][row] + arr[ncol][nrow])
                        if arr[col][row] + arr[ncol][nrow] == 2:
                            print(arr[col][row], arr[ncol][nrow])
                            print(col,row, ncol, nrow)
print('arr')
for i in arr:
    print(i)
#

print('visited')
for i in visited:
    print(i)

print(min(answer_lst))