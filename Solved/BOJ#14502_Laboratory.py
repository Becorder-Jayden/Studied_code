import sys
sys.stdin = open('BOJ#14502_Laboratory.txt')

# 완전 탐색, BFS

from collections import deque
import copy

# U,R,D,L
dcol = [-1,0,1,0]
drow = [0,1,0,-1]

# BFS: 바이러스의 확산
def spread_virus(lst):
    global virus    # 바이러스가 있는 방 정보 가져오기

    queue = deque(virus)
    while queue:
        col, row = queue.popleft()
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]
            if 0<=ncol<N and 0<=nrow<M and lst[ncol][nrow] == 0:
                lst[ncol][nrow] = 2     # 바이러스 확산 표시
                queue.append((ncol, nrow))      # BFS 탐색 전개를 위해 큐 append
    return


def comb(level, start, temp):   # level: 깊이, start: 인덱스 기준, temp: 저장공간
    if level == 3:      # 원하는 깊이에 도달할 때 = 원하는 만큼 담았을 때
        # arr_copy = [arr[i][:] for i in range(N)]    # arr 행에 대해서 n개의 슬라이싱 복사 = deepcopy
        arr_copy = copy.deepcopy(arr)
        cnt = 0     # 안전한 공간의 개수 저장공간
        # 벽을 세우는 작업 진행
        for c, r in temp:
            arr_copy[c][r] = 1


        # 바이러스가 퍼졌을 때 남아있는 방 개수 확인
        spread_virus(arr_copy)
        for col in range(N):
            for row in range(M):
                if arr_copy[col][row] == 0:      # 안전한 공간일 경우
                    cnt += 1                # cnt += 1

        # 정답 리스트에 push 후 초기화
        ans_lst.append(cnt)

        return          # 재귀의 return

    # 조합: 한번 뽑았던 인덱스는 다시 뽑지 않아야 해
    # 뽑은 요소는 temp에 push
    for s in range(start+1, len(possible)):
        comb(level+1, s, temp+[possible[s]])


N, M = map(int, input().split())    # N: 세로, M: 가로
arr = list(list(map(int, input().split())) for _ in range(N))     # 0: 빈칸, 1: 벽, 2:바이러스
possible = []   # 벽을 세울 수 있는 공간 리스트
virus = []      # 바이러스가 있는 공간 리스트
ans_lst = []    # 바이러스가 없는 공간의 개수 리스트

# 벽을 세울 수 있는 모든 공간 담기
for col in range(N):
    for row in range(M):
        if arr[col][row] == 0:
            possible.append((col, row))
        elif arr[col][row] == 2:
            virus.append((col, row))

# 3곳을 뽑아서 진행
comb(0, -1, [])

print(max(ans_lst))

