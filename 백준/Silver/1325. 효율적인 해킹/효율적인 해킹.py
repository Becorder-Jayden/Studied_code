import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adj_lst =[[] for _ in range(N+1)]
ans_lst = [0 for _ in range(N+1)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adj_lst[B].append(A)

def check(idx):
    cnt = 0
    visited = [False for _ in range(N+1)]
    visited[idx] = True
    cnt += 1
    queue = deque()
    queue.append(idx)
    while queue:
        c = queue.popleft()
        for i in adj_lst[c]:
            if visited[i] == False:
                visited[i] = True
                cnt += 1
                queue.append(i)

    return cnt

M = 0
for i in range(1, N+1):
    i_cnt = check(i)
    ans_lst[i] = i_cnt
    if M <= i_cnt:
        M = i_cnt

for i in range(N+1):
    if ans_lst[i] == M:
        print(i, end=' ')
