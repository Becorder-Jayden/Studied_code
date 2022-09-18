import sys
sys.stdin = open('input.txt')

# 9/19, 그냥 하면 안되고 순위를 고려해줘야 하네 : 설계 보강 필요



from collections import deque

def exp(start):
    queue = deque()
    for i in relate[start]:
        queue.append(i)
    dist[start] = -1
    cnt = 0
    while queue:
        cnt += 1
        for i in range(len(queue)):
            pop = queue.popleft()
            if dist[pop] == 0:
                dist[pop] = cnt
                for i in relate[pop]:
                    queue.append(i)

N = int(input())
relate = [[] for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    relate[a].append(b)
    relate[b].append(a)

dist = [0] * (N+1)
for i in range(1, N+1):
    exp(i)
    print(f'#{i}')
    print(relate)
    print(dist)
    dist[i] = 0
    print()
