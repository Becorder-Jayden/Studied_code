import sys
sys.stdin = open('SWEA#1251_OneWay.txt')

# 연결거리를 이용해 가중리 배열 adjM을 만들기
# 최소신장트리 찾기 - 크루즈칼 알고리즘 사용
# 가지치기 보완 가능

def find_set(x):
    while x != P[x]:
        x = P[x]
    return x

def union(x, y):
    P[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    E = float(input())
    P = [i for i in range(N+1)]
    total = 0
    edge = []

    for idx in range(N):
        for vers in range(N):
            edge.append((idx, vers, ((x_li[idx]-x_li[vers])**2 + (y_li[idx]-y_li[vers])**2)**(1/2)))

    edge.sort(key=lambda x : x[2])

    for v, u, w in edge:
        if find_set(v) != find_set(u):
            union(v, u)
            total += w**2

    print(f'#{tc} {round(total*E)}')