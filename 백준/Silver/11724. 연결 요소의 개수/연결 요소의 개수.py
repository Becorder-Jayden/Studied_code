import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True       # 방문 처리
    for i in adj_lst[v]:        # 현재 탐색 인덱스(v)에 있는 요소들 확인
        if not visited[i]:      # 방문 기록이 없으면 DFS 진행
            dfs(i)

N, M = map(int, sys.stdin.readline().split())
adj_lst = [[] for _ in range(N+1)]      # 인접 리스트
visited = [False] * (N+1)       # 방문 리스트
count = 0       # 군집의 개수를 나타낼 변수

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    # 무방향 그래프 등록
    adj_lst[u].append(v)
    adj_lst[v].append(u)

# for문을 돌면서 DFS 진행
for i in range(1, N+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)