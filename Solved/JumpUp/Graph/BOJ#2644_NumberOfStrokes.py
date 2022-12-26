import sys
sys.stdin = open("BOJ#2644_NumberOfStrokes.txt")

# 구글링 참고
# 트리 구조를 그리고 visited 여부 체크
# 시작하는 노드로부터 부모, 자식에 관계없이 촌수를 체크할 수 있다 -> visited는 비교 노드간 거리가 됨

from collections import deque

def bfs(node):
    queue = deque()     # 덱 생성
    queue.append(node)  # 덱에 노드 정보 입력
    while queue:        # 큐가 살아있는 동안
        node = queue.popleft()      # 노트에서 하나의 요소를 빼서
        for i in graph[node]:       # 연결된 노드들에 대해 검사 진행
            if visited[i] == 0:         # 아직 검사되지 않은 노드일 때
                visited[i] = visited[node] + 1      # 기준이 되는 노드의 방문 기록 + 1
                queue.append(i)     # 방문 중인 노드를 큐에 삽입 -> bfs 진행


N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)

if visited[b] > 0:      # x에서 시작한 bfs를 통해 y를 방문할 수 있다면
    print(visited[b])       # y까지의 촌수를 출력
else:                   # 그렇지 못할 경우
    print(-1)               # -1을 출력
