import sys
sys.stdin = open('input.txt')

# 1. 리스트 조합 생성      # 순열 만드는 함수
# 2. 배열 값 계산        # 인덱스를 이용
# 3. 최소값을 출력        # 매개변수로 넘기기 → 시간을 크게 줄일 수 있음


# 0 ~ N 인덱스 리스트 조합 생성하기
def perm(depth, N, S):             # depth: 현재 깊이, N: 최대 깊이, temp: 새롭게 만들어진 배열를 저장하기 위한 임시공간, S: 합계를 저장하는 매개변수
    global ans
    if depth == N:                  # 현재 깊이가 최대 깊이에 도달
        if ans >= S:
            ans = S
        return

    elif S >= ans:                  # 가지치기2
        return

    for i in range(N):                  # 0 ~ N까지 대상
        if visited[i]: continue             # 가지치기 : visited가 표시되어있다면 넘어감
        temp[depth] = i                    # p의 depth 인덱스를 i로 변경
        visited[i] = 1                  # i에 대해 방문 처리
        # print(arr[depth][i])
        perm(depth+1, N, S+arr[depth][i])           # 다음 깊이로 진행, S+arr[depth][i]
        visited[i] = 0                  # 백트래킹을 진행하기 위해 방문 표기를 초기화



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 100*N

    # 0~N 인덱스 리스트 생성하기
    temp = [0] * N
    visited = [0] * N
    perm(0, N, 0)

    print(f'#{tc} {ans}')


# 비트 연산자로 확인하는 방법 visited = 0, 비트연산자 확인해볼 것
'''
def perm(depth, N, S):             # depth: 현재 깊이, N: 최대 깊이, temp: 새롭게 만들어진 배열를 저장하기 위한 임시공간, S: 합계를 저장하는 매개변수
    global ans, visited
    if depth == N:                  # 현재 깊이가 최대 깊이에 도달
        if ans >= S:
            ans = S
        return

    elif S >= ans:                  # 가지치기2
        return

    for i in range(N):                  # 0 ~ N까지 대상
        if visited & 1 << i: continue             # 가지치기 : visited가 표시되어있다면 넘어감
        temp[depth] = i                    # p의 depth 인덱스를 i로 변경
        visited += 1 << i                  # i에 대해 방문 처리
        # print(arr[depth][i])
        perm(depth+1, N, S+arr[depth][i])           # 다음 깊이로 진행, S+arr[depth][i]
        visited -= 1 << i                  # 백트래킹을 진행하기 위해 방문 표기를 초기화



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 100*N

    # 0~N 인덱스 리스트 생성하기
    temp = [0] * N
    visited = 0 
    perm(0, N, 0)

    print(f'#{tc} {ans}')
'''