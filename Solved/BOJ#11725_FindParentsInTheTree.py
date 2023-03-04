import sys
sys.stdin = open('BOJ#11725_FindParentsInTheTree.txt')

#bfs 풀이 - pypy3 정답
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if parent[i] == -1:
                parent[i] = n
                queue.append(i)


N = int(input())
graph = [[] for _ in range(N+1)]
parent = [-1 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

for i in range(2, N+1):
    print(parent[i])




#dfs 풀이 - 오래걸림
sys.setrecursionlimit(10**6)

def find(node):
    for n in graph[node]:
        if parent[n] == -1:
            parent[n] = node
            find(n)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [-1 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

find(1)

for i in range(2, N+1):
    print(parent[i])
