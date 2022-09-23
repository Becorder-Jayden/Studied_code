import sys
sys.stdin = open('input.txt')

# 큐를 이용?
# 9/23 풀지 못함

# 시도 1
'''
from collections import deque

# 상하좌우
dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # N:셀의 개수, M:격리 시간, K:군집의 개수
    arr = [[0]*N for _ in range(N)]
    queue = deque()

    for k in range(K):
        c, r, group, v = map(int, input().split())
        arr[c][r] = (group, v)
        queue.append((c, r, group, v))

    while M > 0:
        M -= 1
        for i in range(len(queue)):
            c, r, group, v = queue.popleft()
            if v == 1:
                if c-1 == 0:
                    queue.append((0, r, group//2, 2))
                else:
                    queue.append((c-1, r, group, 1))
            elif v == 2:
                if c+1 == N:
                    queue.append((N, r, group//2, 2))
                else:
                    queue.append((c+1, r, group, 1))
            elif v == 3:
                if r-1 == 0:
                    queue.append((c, 0, group//2, 4))
                else:
                    queue.append((c, r-1, group, 3))
            elif v == 4:
                if r+1 == N:
                    queue.append((c, N, group//2, 3))
                else:
                    queue.append((c, r+1, group, 4))

    S = 0
    for i in queue:
        S += i[2]
    print(f'#{tc} {S}')
'''

# 시도 2
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # N:셀의 개수, M:격리 시간, K:군집의 개수
    arr = [[0]*N for _ in range(N)]
    queue = deque()

    for k in range(K):
        c, r, group, v = map(int, input().split())
        arr[c][r] = (group, v)
        queue.append((c, r, group, v))