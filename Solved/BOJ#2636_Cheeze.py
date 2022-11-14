import sys
sys.stdin = open('BOJ#2636_Cheeze.txt')

# 구하려는 것 : 치즈가 모두 녹아 없어지는 시간, 모두 녹기 한 시간 전에 남아있는 치즈조각
# 딥카피 연습: copy_arr = [arr[i][:] for i in range(len(arr))]

from collections import deque

dcol = [1, 0, -1, 0]
drow = [0, -1, 0, 1]


# melt() 치즈의 테두리 표시
def melt():
    visited = [[0] * R for _ in range(C)]
    temp_lst = []
    queue = deque()
    queue.append((0, 0))

    while queue:
        col, row = queue.popleft()
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0<=ncol<C and 0<=nrow<R:
                if arr[ncol][nrow] == 0 and visited[ncol][nrow] == 0:
                    visited[ncol][nrow] = 1
                    queue.append((ncol, nrow))
                elif arr[ncol][nrow] == 1:
                    arr[ncol][nrow] = -1
                    temp_lst.append((ncol, nrow))

    for c, r in temp_lst:
        arr[c][r] = 0

    ans_lst.append(len(temp_lst))
    return len(temp_lst)


C, R = map(int, input().split())    # C: 세로, R: 가로
arr = [list(map(int, input().split())) for _ in range(C)]
idx, residue = 0, 0xfff
ans_lst = []

while melt() > 0:
    melt()

for i in range(len(ans_lst)):
    if ans_lst[i] and residue > ans_lst[i]:
        residue = ans_lst[i]
        idx = i+1

print(idx)
print(residue)
