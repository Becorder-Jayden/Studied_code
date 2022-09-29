'''
최소신장트리 - Prim, Kruskal
신장트리 : n개의 정점, n-1개의 간선으로 이루어진 무방향 그래프
최소신장트리 : 간선들의 가중치 합이 최소인 신장트리
간선의 가중치가 모두 다르면 최소신장트리는 1개, 같은 가중치가 있으면 1개 이상 존재

프림 알고리즘 : '간선들을 부모-자식으로 표현한 리스트'에 담아 사용
- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어가는 방식
1) 임의의 정점을 하나 선택해서 시작
2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3) 모든 정점이 선택될 때까지 1, 2 과정 반복

Prim 알고리즘이 크루즈칼보다 빠르다고 알려짐
'''

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def prim1(r, V):
    MST = [0]*(V+1)         # MST 포함여부
    key = [10000]*(V+1)     # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 '가중치'
    key[r] = 0              # 시작정점의 가중치 = 0

    for _ in range(V):      # 시작정점을 이미 선택했기 때문에 남아있는 정점 V개 만큼 진행
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:       # MST에 포함되지 않았고, 가중치가 기본값보다 작을 때
                u = i
                minV = key[i]                       # 해당 정점과 연결된 간선의 가중치를

        MST[u] = 1                  # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])     # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)         # MST 가중치의 합



def prim2(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if MST[i]==1:
                for j in range(V+1):
                    if adjM[i][j]>0 and MST[j]==0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프
    adjL[u].append((v, w))
    adjL[v].append((u, w))
print(adjM)
print(adjL)
print(prim1(0, V))
# print(prim2(0, V))
