import sys
sys.stdin = open('BOJ#11724_ConnectingElements.txt')

# 소스코드 : 무방향 그래프에서 서로 연결된 집단의 개수를 구할 때

def exp(v):
    visited[v] = True   # 현재 노드 방문 처리
    for e in adj[v]:    # 현재 노드와 연결된 다른 노드들을 확인
        if not visited[e]:      # 방문 처리 되지 않읂 노드에 대해서
            exp(e)              # 탐색 진행

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]      # N이 아니라 N+1: 0번 인덱스는 공간을 비워둘 것
visited = [False] * (N+1)       # visited 공간도 N+1개로 생성
cnt = 0

# 주어진 연결 정보를 담아냄
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):     # 1 ~ N+1 인덱스 연결정보에 대해서 확인
    if not visited[i]:      # 방문 처리 되지 않은 노드에 대해 탐색
        exp(i)
        cnt += 1            # 탐색을 마치면 개수 +1
        
print(cnt)