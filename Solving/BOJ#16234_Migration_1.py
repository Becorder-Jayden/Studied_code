import sys
sys.stdin = open('BOJ#16234_Migration.txt')

# 벽을 표시? wall_lst에 담기: find_wall()
# 인구의 이동: migrate(), 큐 구조 사용

# visited를 써야겠구나
# 반례가 있으니 확인해볼 것
'''
4 1 9
96 93 74 30
60 90 65 96
5 27 17 98
10 41 46 20
'''

from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]

# 벽이 사이에 존재하는 두 인덱스 값을 wall_lst에 담아둠
def find_wall():
    global visited
    for col in range(N):
        for row in range(N):
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0<=ncol<N and 0<=nrow<N:
                    if L <= abs(arr[col][row] - arr[ncol][nrow]) <= R:
                        pass
                    else:
                        if [(col,row), (ncol,nrow)] not in wall_lst and [(ncol,nrow), (col,row)] not in wall_lst:
                            wall_lst.append([(col,row), (ncol,nrow)])
                            visited[col][row] += 1
                            visited[ncol][nrow] += 1

# 각 위치에 따라 외부와 연결여부 확인
def open_wall():
    global go

    for col in range(N):
        for row in range(N):
            if (col, row) in [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]:
                if visited[col][row] == 2:
                    visited[col][row] = 0
                else:
                    visited[col][row] = 1
                    go = True
            elif col == 0 or row == 0 or col == N-1 or row == N-1:
                if visited[col][row] == 3:
                    visited[col][row] = 0
                else:
                    visited[col][row] = 1
                    go = True
            else:
                if visited[col][row] == 4:
                    visited[col][row] = 0
                else:
                    visited[col][row] = 1
                    go = True

# 연결된 인덱스의 arr값을 평균을 대치
def migrate(col, row):
    global S, cnt
    if visited[col][row] == 1:
        S, cnt = arr[col][row], 1
        queue = deque()
        queue.append((col, row))
        visited[col][row] = 2
        while queue:
            col, row = queue.pop()
            for v in range(4):
                ncol = col+dcol[v]
                nrow = row+drow[v]
                if 0<=ncol<N and 0<=nrow<N and visited[ncol][nrow] == 1:
                    if L <= abs(arr[col][row] - arr[ncol][nrow]) <= R:
                        visited[ncol][nrow] = 2
                        queue.append((ncol, nrow))
                        S += arr[ncol][nrow]
                        cnt += 1
        # print(S, cnt, S//cnt)

# 하루동안 일어나는 일에 대해 기록
def aday():
    global ans, go, visited, wall_lst
    visited = [[0] * N for _ in range(N)]
    go = False
    wall_lst = []
    find_wall()
    print()
    print('find_wall 이후 visited')
    for i in visited:
        print(*i)


    open_wall()
    print()
    print('open_wall 이후 visited')
    for i in visited:
        print(*i)


    if go == True:
        ans += 1
        for col in range(N):
            for row in range(N):
                migrate(col, row)
                if visited[col][row] == 2:
                    arr[col][row] = S // cnt

    print()
    print(f'ans가 {ans}일 때 arr')
    for i in arr:
        print(*i)


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
wall_lst = []
go = True
ans = 0

while go:
    aday()


print(N, L, R)
print('visited')
# for i in visited:
#     print(*i)
print()
print('arr')
# for i in arr:
#     print(*i)
print()
print(ans)
