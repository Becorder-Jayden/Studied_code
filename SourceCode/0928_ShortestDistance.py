# 최소이동거리
'''
가중치가 부여된 유향 그래프
'간선 1개 = 정점1, 정점2, 가중치값' 필요
[0: (도착정점, 가중치값) ] 형태로 저장
간선완화, 너비우선 탐색을 이용해서 풀이
'''

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 정점은 0번 ~ N번 까지
    G = [[] for _ in range(N+1)]    # 빈리스트를 생성
    for _ in range(E):
        u, v, weight = map(int, input().split())
        # 유향그래프, 정점과 가중치를 묶어서 저장
        G[u].append( (v,weight) )
    D = [0xfffff] * (N+1)          # 거리를 저장하는 리스트, 방문 정보가 필요 x
    D[0] = 0                       # cf. 초기값 주의, 출발점 항상 0으로 설정
    Q = [0]

    while Q:
        u = Q.pop(0)
        for v, weight in G[u]:      # v: 인접 정점
            # (u, v) 간선완화
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                Q.append(D[v])

    # def dfs(u):
    #    # 절대 까먹지 마세요, 핵심로직
    #    for v, weight in G[u]:  # v: 인접 정점
    #         if D[v] > D[u] + weight:            # 절대 까먹지 마세요, 핵심로직
    #             D[v] = D[u] + weight
    #             dfs(v)
    #
    # dfs(0)

    print(f'#{tc} {D[N]}')


