import sys
sys.stdin = open('../Solving/input.txt')

# 다익스트라로 풀어야 함 → 최단경로 : 다익스트라 알고리즘
# 크루즈칼 : 서로소 집합
# 크루즈칼 + 짧은 경로 : 다익스트라

def dijkstra(s, V):     # 시작 정점, 정점의 개수
    U = [0] * (V+1)         # 확인 여부를 표시
    U[s] = 1                # 출발 정점 확인
    for i in range(V+1):
        D[i] = adjM[s][i]

    for _ in range(V):
        minV = 0xfffff
        w = 0                                   # 인접 정점들 중 최소 가중치인 곳을 탐색하는 과정
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:       # 확인되지 않았고, 가중치가 초기값보다 작을 경우
                minV = D[i]
                w = i

        U[w] = 1                # 확인 표시
        for v in range(V+1):
            if 0 < adjM[w][v] < 0xfffff:
                D[v] = min(D[v], D[w] + adjM[w][v])

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())    # 정점, 간선의 개수
    adjM = [[0xfffff]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        adjM[i][i] = 0              # 자기 자신으로 향하는 경로의 비용(거리) 0 세팅

    for n in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w                          # s → e 방향에 대한 가중치 설정

    D = [0] * (N+1)
    dijkstra(0, N)

    print(f'#{tc} {D[N]}')
