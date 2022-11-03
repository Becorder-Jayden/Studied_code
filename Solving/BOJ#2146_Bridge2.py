import sys
sys.stdin = open('BOJ#2146_Bridge.txt')

# 경계면 찾기 섬 구분 하기 합쳐보기
# deepcopy가 메모리를 많이 먹는 듯?
# 평소 하던 것.
#


from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0xffff
border_lst = []
# answer_lst = []

# 섬 구분하기
def divide_island():
    cnt = 0
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:
                cnt -= 1
                queue = deque()
                queue.append((col, row))
                while queue:
                    for i in range(len(queue)):
                        col, row = queue.popleft()
                        arr[col][row] = cnt
                        for v in range(4):
                            ncol = col + dcol[v]
                            nrow = row + drow[v]
                            if 0 <= ncol < N and 0 <= nrow < N and arr[ncol][nrow] == 1:
                                arr[col][row] = cnt
                                queue.append((ncol, nrow))
                for v in range(4):
                    ncol = col+dcol[v]
                    nrow = row+drow[v]
                    if 0<=ncol<N and 0<=nrow<N:
                        if arr[ncol][nrow] == 0:        # 주변값으로 0을 갖는 곳
                            arr[col][row] = -1          # 섬의 경계면 표시
            # 경계로 표시된 곳의 인덱스를 border_lst에 담음
            if arr[col][row] < 0:
                border_lst.append((col, row))


# 경계면 찾기
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
            if arr[col][row] < 0:
                border_lst.append((col, row))


# 진행
divide_island()     # 섬 구분하기
visited = [arr[i][:] for i in range(len(arr))]
# find_border()       # 경계면 찾기

# for i in visited:
#     print(i)
# print('border_lst:', border_lst)


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

                elif visited[col][row] < 0 and visited[ncol][nrow] < 0 and visited[col][row] != visited[ncol][nrow]:
                    if arr[col][row] < 0 and arr[ncol][nrow] > 0:
                        # answer_lst.append(arr[ncol][nrow])
                        if arr[ncol][nrow] < answer:
                            answer = arr[ncol][nrow]
                    elif arr[col][row] > 0 and arr[ncol][nrow] < 0:
                        # answer_lst.append(arr[col][row])
                        if 0<arr[col][row] < answer:
                            answer = arr[col][row]
                    elif arr[col][row] > 0 and arr[ncol][nrow] > 0:
                        # answer_lst.append(arr[col][row] + arr[ncol][nrow])
                        if 0<arr[col][row] + arr[ncol][nrow] < answer:
                            answer = arr[col][row] + arr[ncol][nrow]
                            print(answer)
                            print(col, row, ncol, nrow)


print('arr')
for i in arr:
    print(i)
print()
# 섬 경계면 표시
for i in visited:
    print(i)
print()
# print(answer_lst)
# print(answer_lst[0])
print(answer)

