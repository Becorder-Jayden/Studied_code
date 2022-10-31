import sys
sys.stdin = open('SWEA#1217.involution.txt')

# N의 M 거듭제곱 값을 재귀호출로 구현
def dfs(N, level, val):
    if level == M:
        print(val)
        return
    dfs(N, level+1, val*N)

for i in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    print(f'#{tc}', end=' ')
    dfs(N, 0, 1)