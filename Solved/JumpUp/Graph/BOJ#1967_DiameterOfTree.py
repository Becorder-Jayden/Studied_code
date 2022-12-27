# recursionError가 발생하면 setrecursionlimit을 먼저 적용해보자
# 루트노드로부터 가장 먼 지점(가중치의 합)이 가장 큰 지점을 찾는 과정을 두번 반복
# visited를 음수값으로 설정하고 확인할 때마다 값을 바꿔준다면 방문 여부의 확인과 함께 거리를 나타낼 수 있다

import sys
sys.stdin = open('BOJ#1967_DiameterOfTree.txt')
sys.setrecursionlimit(10**6)    # 최대 재귀 깊이를 늘려주는 코드

def dfs(node, weight):
    for n, w in graph[node]:
        if visited[n] == -1:        # 확인한 적이 없는 노드에 대해
            visited[n] = weight + w     # 이전까지의 가중치 + 현재의 가중치
            dfs(n, weight + w)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
for _ in range(N-1):
    x, y, w = map(int, input().split())
    graph[x].append([y, w])
    graph[y].append([x, w])

# 첫번째 탐색
dfs(1, 0)   # 루트 노드에서 가장 먼 노트(far_node)를 찾음

# 두번째 탐색을 위한 준비
far_node = visited.index(max(visited))
visited = [-1] * (N+1)      # visited 초기화
visited[far_node] = 0

# 두번째 탐색
dfs(far_node, 0)    # far_node로부터 가장 먼 노드를 찾음

# 계산과정 줄이기
# far_node = visited.index(max(visited))
# print(visited[far_node])

print(max(visited))
