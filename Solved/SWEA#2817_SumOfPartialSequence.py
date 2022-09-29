import sys
sys.stdin = open('../Solving/input.txt')

def exp(k, S):         # k: 인덱스, S: 합계
    global ans              # ans 전역 변수를 불러옴
    if k == N:              # 탐색하고 있는 인덱스가 N번 인덱스 → 리프노드에서 값을 확인했을 때
        if S == K:              # 합계가 K와 같을 경우 ans += 1
            ans += 1
    else:                       # 다음 하위노드를 탐색
        exp(k+1, S+li[k])       # 현재의 값을 선택했을 경우, S에 현재 값을 더함
        exp(k+1, S)             # 현재 값을 선택하지 않았을 경우


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())            # N개의 자연수가 주어짐, 합이 최소 K가 되는 경우의 수
    li = list(map(int, input().split()))
    ans = 0
    exp(0, 0)
    print(f'#{tc} {ans}')