import sys
sys.stdin = open('../Solving/input.txt')

# 크루즈칼, prim1, prim2 방식 비교
# 개인적으로는 크루즈칼이 편하다..
# 파이썬에서는 disjoint-set만 구현할 수 있으면 크루즈칼이 편하다고 하심.

# 크루즈칼 ***
def find_set(x):
    while x!= G[x]:
        x = G[x]
    return x

def union(x, y):
    G[find_set(x)] = find_set(y)


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [i for i in range(V+1)]
    adjL = []

    for e in range(E):
        n1, n2, w = map(int, input().split())
        adjL.append([n1, n2, w])

    adjL.sort(key=lambda x : x[2])          # 가중치를 기준으로 오름차순 정렬

    ans = 0
    for n1, n2, w in adjL:
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            ans += w                # 집합을 만들면서 결합되는 w를 더해감

    print(f'#{tc} {ans}')



# # Prim1
# def prim1(start, V):        # 시작위치(어느 정점을 선택해도 괜찮아), 정점의 개수
#     MST = [0] * (V+1)
#     key = [10000] * (V+1)
#     key[start] = 0
#
#     for _ in range(V):      # 시작위치를 제외한 V만큼 반복
#         u = 0
#         minV = 10000
#         # prim1 vs prim2 : MST 표시가 없는 것 기준 // 있는것 기준 탐색 진행
#         for i in range(V+1):
#             if MST[i] == 0 and key[i] < minV:        # 인덱스가 확인되지 않았고, 해당 가중치가 기준보다 작을 경우
#                 minV = key[i]                           # cf. minV가 최소값을 가지고 있는 '한 지점'을 잡아내기 위해
#                 u = i                                   # 탐색을 진행하면서 u 인덱스를 찾음
#         MST[u] = 1          # u 인덱스 확인 여부 표시
#
#         for v in range(V+1):
#             if MST[v] == 0 and adjM[u][v] > 0:      # 방문하지 않은 정점들에 대해, 가중치가 있는 경우(간선이 존재)
#                 key[v] = min(key[v], adjM[u][v])
#
#     return sum(key)
#
#
# for tc in range(1, int(input())+1):
#     V, E = map(int, input().split())
#     G = [i for i in range(V+1)]
#     adjM = [[0] * (V+1) for _ in range(V+1)]
#
#     for e in range(E):
#         n1, n2, w = map(int, input().split())
#         adjM[n1][n2] = w
#         adjM[n2][n1] = w
#
#     print(f'#{tc} {prim1(2, V)}')

# # prim2
# def prim2(start, V):    # 어느 한 시작 정점(어느 위치든), 정점의수
#     MST = [0] * (V+1)
#     MST[start] = 1          # 확인 표시
#
#     s = 0
#     for _ in range(V):      # 시작 위치를 제외한 V만큼 반복
#         u = 0
#         minV = 0xfffff
#         for i in range(V+1):
#             # prim1 vs prim2 차이
#             if MST[i] == 1:
#                 for j in range(V+1):
#                     if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
#                         u = j
#                         minV = adjM[i][j]
#
#         s += minV
#         MST[u] = 1          # u 인덱스 확인 처리
#     return s
#
# for tc in range(1, int(input())+1):
#     V, E = map(int, input().split())
#     G = [i for i in range(V+1)]
#     adjM = [[0] * (V+1) for _ in range(V+1)]
#
#     for e in range(E):
#         n1, n2, w = map(int, input().split())
#         adjM[n1][n2] = w
#         adjM[n2][n1] = w
#
#     print(f'#{tc} {prim2(2, V)}')