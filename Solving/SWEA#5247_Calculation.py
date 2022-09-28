import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 0
    visit[start] = 0
    while queue:
        cnt += 1
        for i in range(len(queue)):
            q = queue.popleft()
            if q == M:
                return
            for i in [q+1, q-1, q*2, q-10]:
                if 0<=i<maxLimit and visit[i] > cnt:
                    visit[i] = cnt
                    queue.append(i)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    maxLimit = 1000001
    visit = [maxLimit] * (maxLimit+1)
    bfs(N)
    print(f'#{tc} {visit[M]}')