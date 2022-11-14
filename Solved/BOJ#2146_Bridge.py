import sys
sys.stdin = open('../Solving/BOJ#1799_Bishop.txt')


# 간척사업 아이디어 적용
# 섬의 경계면을 중복되지 않게 border_lst에 담기 → flag 활용
# 체크용 arr를 2개 이상 사용할 때도 있다
# 






from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]


def divide_island():
    cnt = 1
    # 주어진 arr의 모든 부분 탐색 시도
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:      # 어느 한 섬에 도달하면
                cnt += 1                # 몇 번째 섬인지 표시하기 위해 cnt 활용
                queue = deque()             # BFS 진행
                queue.append((col, row))
                checked[col][row] = 1

                while queue:
                    # 메모리 체크
                    # print(len(queue), queue)
                    # print(len(border_lst), border_lst)

                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        arr[col][row] = cnt
                        flag = 0                        # 중복해서 border_lst에 들어가는 것을 방지하기 위한 체커

                        for v in range(4):
                            ncol = col+dcol[v]
                            nrow = row+drow[v]
                            if 0<=ncol<N and 0<=nrow<N:
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
    cnt = 0
    while queue:
        # 메모리 체크
        # print(queue)
        cnt += 1
        for i in range(len(queue)):
            col, row = queue.popleft()
            for v in range(4):
                ncol = col + dcol[v]
                nrow = row + drow[v]
                if 0<=ncol<N and 0<=nrow<N:
                    if arr[ncol][nrow] == 0 and visited[ncol][nrow] == 0:
                        arr[ncol][nrow] = arr[col][row]
                        visited[ncol][nrow] = cnt
                        checked[ncol][nrow] = 1
                        queue.append((ncol, nrow))

                    if arr[col][row] != arr[ncol][nrow]:
                        if visited[col][row] == 0 and visited[ncol][nrow]:
                            temp = visited[ncol][nrow]
                        elif visited[ncol][nrow] == 0 and visited[col][row]:
                            temp = visited[col][row]
                        else:
                            temp = visited[col][row] + visited[ncol][nrow]

                        if answer > temp:
                            answer = temp

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
checked = [[0]*N for _ in range(N)]
answer = 0xfff
border_lst = []
ans_lst = []


divide_island()
expand()


print(answer)



'''
clean ver.
# cnt 변수를 사용하지 않음
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

'''