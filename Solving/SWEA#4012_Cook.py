import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 하아.. x 09/30

# 순열로 조합가능한 집합 만들기
def perm(depth, N, S=0):
    global visited, ans
    if depth == N:
        A, B = temp[:N//2], temp[N//2:]
        print(A, B)
        # print(arr[A[0]][A[1]] + arr[A[1]][A[0]])
        # print(arr[B[0]][B[1]] + arr[B[1]][B[0]])
        return

    for i in range(N):
        if visited & (1 << i): continue
        visited += 1 << i
        temp[depth] = i
        perm(depth+1, N)
        visited -= 1 << i


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = 0
    temp = [0] * N
    ans = 0
    perm(0, N, 0)

    for i in arr:
        print(i)
