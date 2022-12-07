import sys
sys.stdin = open('BOJ#16234_Migration.txt')

# BFS 탐색을 통해 그룹별로 번호 지정
# visited 기록

from collections import deque

# 상, 우, 하, 좌
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def isGroup(col, row):
    global group_cnt
    group_cnt += 1
    queue = deque()
    queue.append((col, row))
    group[col][row] = group_cnt
    while queue:
        for i in range(len(queue)):
            col, row = queue.popleft()
            visited[col][row] = 1
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0<=ncol<N and 0<=nrow<N:
                    if L <= abs(arr[col][row]-arr[ncol][nrow]) <= R and visited[ncol][nrow] == 0:
                        queue.append((ncol, nrow))
                        group[ncol][nrow] = group_cnt
                        visited[ncol][nrow] = 1

def sum_group():
    for col in range(N):
        for row in range(N):
            sum_list[group[col][row]] += arr[col][row]
            cnt_list[group[col][row]] += 1


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
group = [[0] * N for _ in range(N)]
group_cnt = 0
for col in range(N):
    for row in range(N):
        if visited[col][row] == 0:
            isGroup(col, row)

sum_list = [0]*(group_cnt+1)
cnt_list = [0]*(group_cnt+1)
sum_group()
avg_list = [0]*(group_cnt+1)
for i in range(1, group_cnt+1):
    avg_list[i] = sum_list[i]//cnt_list[i]

for i in range(group_cnt+1):
    for col in range(N):
        for row in range(N):
            if group[col][row] == i:
                arr[col][row] = avg_list[i]


for i in arr:
    print(*i)
# for i in visited:
#     print(*i)
# for i in group:
#     print(*i)