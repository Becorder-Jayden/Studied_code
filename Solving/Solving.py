import sys
sys.stdin = open("input.txt")


# from collections import deque
#
# # N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시 번호
# N, M, K, X = map(int, sys.stdin.readline().split())
# A = [[] for i in range(N+1)]
# answer = []
# visited = [-1] * (N + 1)
#
# def bfs(v):
#     queue = deque()
#     queue.append(v)
#     visited[v] += 1
#     while queue:
#         check = queue.popleft()
#         for i in A[check]:
#             if visited[i] == -1:
#                 visited[i] = visited[check] + 1
#                 queue.append(i)
#
# for _ in range(M):
#     S, E = map(int, sys.stdin.readline().split())
#     A[S].append(E)
#
# bfs(X)
#
# for i in range(N+1):
#     if visited[i] == K:
#         answer.append(i)
#
# if not answer:
#     print(-1)
# else:
#     answer.sort()
#     for i in answer:
#         print(i)