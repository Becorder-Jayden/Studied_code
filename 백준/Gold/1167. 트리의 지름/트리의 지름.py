from collections import deque

N = int(input())

# 연결 노드를 사용할 때 1번 인덱스에 1번 값이 들어갈 수 있도록 여유분: N+1 만큼
adj_lst = [[] for _ in range(N+1)]
dist_lst = [0] * (N+1)
visited_lst = [False] * (N+1)

# 인접 리스트 생성
for i in range(N):
    arr = list(map(int, input().split()))
    idx = int(arr[0])
    link = arr[1:]
    for i in range(0, len(link)//2):
        adj = link[2*i]
        dist = link[2*i+1]
        adj_lst[idx].append((adj, dist))

def bfs(idx):
    queue = deque()
    queue.append(idx)
    visited_lst[idx] = True
    while queue:
        node = queue.popleft()
        for i in adj_lst[node]:
            if not visited_lst[i[0]]:
                visited_lst[i[0]] = True
                dist_lst[i[0]] = i[1] + dist_lst[node]
                queue.append(i[0])

bfs(1)      # 1이 아닌 어떠한 값에서도 탐색 가능

max_idx = 0
for i in range(N+1):
    if dist_lst[max_idx] < dist_lst[i]:
        max_idx = i

visited_lst = [False] * (N+1)
dist_lst = [0] * (N+1)
bfs(max_idx)

print(max(dist_lst))

