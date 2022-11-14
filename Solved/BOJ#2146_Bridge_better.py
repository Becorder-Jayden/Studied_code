import sys
sys.stdin = open('BOJ#2146_Bridge.txt')

from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]


def divide_island():
    cnt = 1
    # 주어진 arr의 모든 부분 탐색 시도
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:  # 어느 한 섬에 도달하면
                cnt += 1
                queue = deque()
                queue.append((col, row))
                checked[col][row] = 1
                while queue:
                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        arr[col][row] = cnt
                        flag = 0
                        for v in range(4):
                            ncol = col + dcol[v]
                            nrow = row + drow[v]
                            if 0 <= ncol < N and 0 <= nrow < N:
                                if arr[ncol][nrow] and checked[ncol][nrow] == 0:
                                    arr[col][row] = cnt
                                    checked[ncol][nrow] = 1
                                    queue.append((ncol, nrow))

                                if arr[ncol][nrow] == 0:
                                    if flag > 0:
                                        continue
                                    border_lst.append((col, row))
                                    flag += 1
def expand():
    global answer
    queue = deque()
    queue.extend(border_lst)
    while queue:
        # print(queue)  # 메모리 체크
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0 <= ncol < N and 0 <= nrow < N:
                    # print(ncol, nrow)
                    if arr[ncol][nrow] == 0:
                        arr[ncol][nrow] = arr[col][row]
                        visited[ncol][nrow] = visited[col][row] + 1     # cnt 변수를 사용하지 않아도 된다

                        queue.append((ncol, nrow))

                    if arr[col][row] != arr[ncol][nrow]:
                        temp = visited[col][row] + visited[ncol][nrow]
                        if answer > temp:
                            answer = temp


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
checked = [[0] * N for _ in range(N)]
answer = 0xfff
border_lst = []
ans_lst = []

divide_island()
expand()


print(answer)
