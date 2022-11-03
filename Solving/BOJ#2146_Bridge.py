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
                cnt += 1
                queue = deque()
                visited[col][row] = cnt           # queue에 집어 넣을 때 해야 중복방문 x? try? : x
                queue.append((col, row))
                while queue:
                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        arr[col][row] = cnt
                        out = 0             # 경계선 체크
                        for v in range(4):
                            ncol = col+dcol[v]
                            nrow = row+drow[v]
                            if 0<=ncol<N and 0<=nrow<N:
                                if arr[ncol][nrow] == 1:
                                    arr[col][row] = cnt
                                    visited[ncol][nrow] = cnt
                                    queue.append((ncol, nrow))      #
                                elif arr[ncol][nrow] == 0:
                                    visited[col][row] = cnt
                                    # if visited[col][row]:
                                    #     border_lst.append((col, row))
                        arr[col][row] = 0   # 다리가 1칸으로 충분할 때를 위한 변경

    # col, row for문을 빼자니 누락되는 값이 있고, 안하자니 메모리 초과(?)이고..
    # for col in range(N):
    #     for row in range(N):
    #         # 경계면 리스트에 담기
    #         if visited[col][row]:
    #             border_lst.append((col, row))


            # 경계면 리스트에 담기
            if visited[col][row]:
                border_lst.append((col, row))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = 0xfff

border_lst = []

# 섬 구분
divide_island()

queue = deque()
queue.extend(border_lst)


# print('queue', queue)
#
# for i in visited:
#     print(i)

cnt = 0
while queue:
    cnt += 1
    for i in range(len(queue)):
        col, row = queue.popleft()
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0<=ncol<N and 0<=nrow<N:
                # (arr, visited) 가 비어있는곳(바다)로의 경로 탐색
                if arr[ncol][nrow] == 0 and visited[ncol][nrow] == 0:
                    arr[ncol][nrow] = cnt   # 가장 가까운 섬에서 바다까지의 거리
                    visited[ncol][nrow] = visited[col][row]   # 어느 섬으로부터 visited 되었는지 기록
                    queue.append((ncol, nrow))

                # 현재 기록하려는 visited가 이미 채워져있고, 이전에 본 visited와 이미 기록된 visited의 값이 다를 때
                elif visited[ncol][nrow] and visited[ncol][nrow] != visited[col][row]:
                    # print(arr[col][row] + arr[ncol][nrow])
                    prev_pres_add = arr[col][row] + arr[ncol][nrow]
                    if answer > prev_pres_add:
                        answer = prev_pres_add
                        # break

# print(border_lst)
# 경계를 기준으로 탐색 진행


# print('arr')
# for i in arr:
#     print(i)
# # print(border_lst)
#
# print()
# print('visited')
# for i in visited:
#     print(i)
# print()
#
if answer == 0xfff:
    answer = 0

print(answer)