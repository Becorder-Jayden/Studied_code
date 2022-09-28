'''
간선을 하나씩 선택해서 MST를 찾는 알고리즘
1) 모든 간선을 가중치에 따라 오름차순 정렬
2) 가중치가 낮은 간선부터 선택하면서 트리를 증가
3) n-1개의 간선이 선택될가지 2) 반복
프림은 정점의 개수가 많아지면 느려지는 단점이 있음. 크루스칼이 좀더 효율적, 최종적으로 사용
'''

# 대표원소 찾기
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

# 대표원소를 바꿈
def union(x, y):
    rep[find_set(y)] = find_set(x)




V, E = map(int, input().split())    # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, v, u])                  # w가 앞에온 이유: sort()로 정렬을 적용하기 위해(람다식 안쓰기위해)
edge.sort()
rep = [i for i in range(V+1)]       # 대표원소 배열

N = V + 1   # 실제 정점의 개수
cnt = 0     # 선택한 edge의 수
total = 0   # MST 가중치의 합

for w, v, u in edge:
    if find_set(v) != find_set(u):      # 정점이 다를 때 진행
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:  # MST 구성이 끝나면
            break
print(total)
