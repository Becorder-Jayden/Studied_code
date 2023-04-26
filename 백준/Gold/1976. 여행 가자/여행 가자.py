N = int(input())
M = int(input())
city = [[0 for j in range(N+1)] for i in range(N+1)]

# find: 대표 노드 찾기
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

# union: b의 대표노드를 a의 대표 노드로 변경
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# city 연결 데이터 저장
for i in range(1, N+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)

# 여행 도시 정보 저장
route = list(map(int, input().split()))
route.insert(0, 0)  # 0번 인덱스에 0을 추가

parent = [0] * (N+1)

# 대표 노드를 자기 자신으로 초기화
for i in range(1, N+1):
    parent[i] = i

# 연결되어 있을 때 부모 노드를 변경 (b의 부모노드를 a의 부모로 대체)
for i in range(1, N+1):
    for j in range(1, N+1):
        if city[i][j] == 1:
            union(i, j)

# 부모노드가 모두 동일한지 확인
index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")
