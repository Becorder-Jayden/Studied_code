import sys
sys.stdin = open('BOJ 2606.txt')    # 바이러스

# visited 방문처리를 해주고, 해당 정점과 연결된 간선을 따라 dfs 적용
def dfs(start):
    visited[start] = 1
    for connected in graph[start]:
        if visited[connected] == 0:
            dfs(connected)
    return visited

T = int(input())

# DFS 풀이를 위해 graph와 visited 준비
graph = [[] for t in range(T+1)]
visited = [0 for t in range(T+1)]

N = int(input())
for n in range(N):
    # 입력된 값을 기준으로 간선을 연결
    start, end = map(int, input().split())
    graph[start] += [end]
    graph[end] += [start]


dfs(1)

print(graph)
print(visited)

# 방문한곳(visited == 1)인 부분의 개수를 찾아 정답으로 출력
# cf. 시작점을 포함한 채 answer가 계산되므로 출력값에 주의
answer = 0
for i in visited:
    if i == 1:
        answer += 1
print(answer-1)