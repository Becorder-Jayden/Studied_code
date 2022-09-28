'''
6 8         마지막 정점번호(0번부터 시작), E 간선수
0 1 0 2 0 5 0 6 3 4 3 5 6 4 5 4
'''

# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# # 인접행렬
# adjM = [[0]*(V+1) for _ in range(V+1)]      # 인접 행렬
# adjList = [[] for _ in range(V+1)]          # 인접 리스트
#
#
# for i in range(E):
#     n1, n2 = arr[i*2], arr[i*2+1]
#     adjM[n1][n2] = 1
#     adjM[n2][n1] = 1            # 방향이 없는 경우에만
#
#     adjList[n1].append(n2)
#     adjList[n2].append(n1)


# 상원이의 친구관계 문제
# # dfs
# def dfs(i, N, c):       # i:현재 보고있는 사람, c: 친구 경로
#     if c == 3:
#         return
#     visited[i] = 1
#     for j in range(1, N+1):
#         if adjM[i][j] and visited[j] == 0:      # i번과 친구이고, 초대장을 받지 않은 친구가 있다면
#             dfs(j, N, c+1)
# 
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     adjM = [[0]*(N+1) for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         adjM[a][b] = 1
#         adjM[b][a] = 1
#     visited = [0] * (N+1)
#     dfs(1, N, 0)
# 
#     print(f'#{tc} {sum(visited)-1}')
    
# bfs 풀이
def bfs(N):
    q = [1]    # 큐 생성
    visited = [0]*(N+1)    # visited 생성
    visited[1] = 1    # 시작점 방문표시
    while q:        # 큐가 비어있지 않으면
        t = q.pop(0)

    
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
    visited = [0] * (N+1)
    bfs(1, N, 0)

    print(f'#{tc} {sum(visited)-1}')
    
    