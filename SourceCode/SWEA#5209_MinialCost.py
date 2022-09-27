import sys
sys.stdin = open('../Solving/input.txt')

def perm(depth, N, visited=0, temp=0):
    global ans
    if depth == N:              # 순열의 깊이가 N에 도달했을 때
        if ans > temp:              # 정답이 임시값보다 크다면
            ans = temp              # 임시값을 정답으로 해서 최소화
        return

    elif temp >= ans:           # 임시값이 정답보다 클 때: 가지치기
        return

    for i in range(N):
        print('visited:', visited)
        print('1<<i:', 1<<i)
        print('visited & (1<<i):', visited & (1<<i))
        print()
        if visited & (1<<i):
            continue
        visited += 1 << i
        perm(depth+1, N, visited, temp+arr[depth][i])
        visited -= 1 << i

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    ans = 100*N
    perm(0, N)

    print(f'#{tc} {ans}')