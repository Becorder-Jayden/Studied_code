from collections import deque

N = int(input())
graph = [i for i in range(1, N+1)]

queue = deque(graph)

for i in range(N-1):
    queue.popleft()
    sec = queue.popleft()
    queue.append(sec)

print(queue[0])
