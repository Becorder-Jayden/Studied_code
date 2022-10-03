import sys
sys.stdin = open('../Solving/input.txt', encoding='UTF-8')

## 아직 못품 !!! 9/30
## 지지부진.. 중단..




# 연화 코드..
def comb(d, v):        # d = 남은 피연산자 개수, v = 현재 값
    global mxv, mnv
    if d == N:            # 연산 끝나면 최댓값, 최솟값 갱신
        if mxv < v:
            mxv = v
        if mnv > v:
            mnv = v
        return

    for i in range(4):        # 네 개의 연산자 종류만큼 순회
        if calc[i] != 0:        # 연산자의 개수가 남아있으면
            calc[i] -= 1
            exv = v                # 재귀 빠져나올 때 원상복귀하기 위한 값
            if i == 0:
                v += nums[d]
            elif i == 1:
                v -= nums[d]
            elif i == 2:
                v *= nums[d]
            else:
                v /= nums[d]
                v = int(v)
            comb(d+1, v)
            calc[i] += 1
            v = exv            # 원상복귀


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    calc = list(map(int, input().split()))  # +, -, *, // 순서대로 연산자 개수
    nums = list(map(int, input().split()))
    mxv = -100000001
    mnv = 100000001
    comb(1, nums[0])
    print(f'#{testcase} {mxv-mnv}')
