import sys
sys.stdin = open('SWEA#4012_Cook.txt')

# N이 6개 이상일 때는 어떻게 해야 하는건지 모르겠음..

# N개의 숫자 중 N//2개 선택
def perm(i, k):
    if i == k:
        ret = []
        a, b = temp[:N//2], temp[N//2:]
        for j in range(N//2):
            ret.append(arr[a[j]][b[j]] + arr[b[j]][a[j]])
        print(ret)

    for j in range(k):
        if visited[j] == 0:
            visited[j] = 1
            temp[i] = idx[j]
            perm(i+1, N)
            visited[j] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [i for i in range(N)]
    temp = [0] * N
    visited = [0] * N

    perm(0, N)
