import sys
sys.stdin = open('BOJ#15654_N&M(5).txt')

def perm(level, temp):
    if level == M:
        print(*temp)
        return
    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        perm(level+1, temp+[arr[i]])
        visited[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N
perm(0, [])

# print(N, M)
# print(arr)