# 인수의 생일파티 예시
'''
인수의 집 → 나머지 집으로 가는 시간을 표에 정리
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''

# 다익스트라 생성
def dijikstra(N, X, adj, d):              # N, X:, adj, d
    for i in range(N+1):
        d[i] = adj[X][i]
    U = [X]
    for _ in range(N-1):                # N개의 정점 중 출발을 제외한 정점 선택, 하나를 이미 선택해서 U에 넣었으니깐 하나 뺀 개수만큼 진행 가능
        w = 0
        for i in range(1, N+1):
            if (i not in U) and d[i] < d[w]:        # 남은 노드 중 비용이 최소인 w
                w = i
        U.append(w)
        for v in range(1, N+1):                 # 정점 i가
            if 0 < adj[w][v] < 100000:          # w에 인접이면, 0이면 자기 자신을 가리킴, 100000이면 무한인 비용지점
                d[v] = min(d[v], d[w]+adj[w][v])

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[1000000]*(N+1) for _ in range(N+1)]        # 무한으로 비용을 설정해서 인접행렬을 만듬
    for i in range(N+1):                # 대각선상 비용 0
        adj1[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c

    dout = [0] * (N+1)
    dijikstra(N, X, adj1, dout)
    # print(dout)     # 최소 비용을 찾음

    # din을 만들어서 다익스트라를 돌리면 들어오는 방향에 대해서도 찾을 수 있다 -> 정답