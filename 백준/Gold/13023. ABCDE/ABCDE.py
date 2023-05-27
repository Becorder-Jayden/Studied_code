def dfs(v, depth):
    global arrived
    if depth == 5:          # 최대 깊이가 5에 도달할 경우
        arrived = True      # arrived 표기 True로 전환
        return

    visited[v] = True       # 탐색 중인 v에 대해 True 처리ㅁ

    for i in adj_lst[v]:    # v의 인접 요소 탐색
        if not visited[i]:      # 방문한 적이 없는 v일 때 
            dfs(i, depth + 1)       # dfs 진행

    visited[v] = False      # v에 대한 탐색이 끝나면 False 처리

N, M = map(int, input().split())
adj_lst = [[] for _ in range(N)]
visited = [False] * (N+1)
arrived = False

for i in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

count = 0
for i in range(N):
    dfs(i, 1)       # 각 i에 대해 dfs 탐색 진행
    if arrived:     # arrived 표기가 True일 때 탐색 종료
        break

if arrived:
    print(1)
else:
    print(0)