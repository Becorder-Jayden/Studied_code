import sys
sys.stdin = open('input.txt')

def backtrack(k, cur_sum):
    global ans
    if cur_sum > hap:       # 가지치기: 이미 선택한 값들의 합이 목표치인 hap보다 클 경우
        return
    if k == N:
        if cur_sum == hap:
            ans += 1
    else:
        backtrack(k+1, cur_sum + arr[k])
        backtrack(k+1, cur_sum)

T = int(input())
for tc in range(1, T+1):
    N, hap = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    backtrack(0, 0)
    print(f'#{tc} {ans}')