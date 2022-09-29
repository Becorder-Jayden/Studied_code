import sys
sys.stdin = open('../Solving/input.txt')

def find_set(x):
    while x != G[x]:                # x가 포함된 집합의 대표 정점을 찾음
        x = G[x]
    else:
        return x

def union(x, y):
    G[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    G = [i for i in range(N+1)]                         # N개의 집합 노드를 생성
    arr = list(map(int, input().split()))

    for i in range(M):
        x, y = arr[2*i], arr[2*i+1]
        if find_set(x) != find_set(y):                  # 그룹을 짓기 전 대표 정점이 같은지 확인
            union(x, y)                                 # 같지 않을 때 union 진행
            N -= 1                                      # 그룹이 지어지면 전체 중 대표 정점의 수 1 감소

    print(f'#{tc} {N}')
