import sys
sys.stdin = open('BOJ 2589.txt')


# pypy3로 풀면 정답, python3로 풀면 시간초과
# 최단거리에 대한 조건이 주어지는 탐색에는 bfs 활용

from collections import deque

dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

cols, rows = map(int, input().split())
arr = [list(input()) for col in range(cols)]

def bfs(col, row):
    queue = deque()
    queue.append((col, row))
    visited[col][row] = 1
    cnt = 0
    while queue:
        cnt += 1        # 같은 레벨의 노드 진행이 마무리 될 때마다 cnt 증가
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0<=ncol<cols and 0<=nrow<rows and arr[ncol][nrow] == 'L' and visited[ncol][nrow] == 0:
                    visited[ncol][nrow] = 1
                    queue.append((ncol, nrow))
    return cnt

li = []
for col in range(cols):
    for row in range(rows):
        if arr[col][row] == 'L':
            visited = [[0] * rows for col in range(cols)]
            li.append(bfs(col, row))

# 시작점을 포함하지 않는 값을 답으로 출력 : 이동하는데 걸리는 시간을 구하므로
print(max(li)-1)
