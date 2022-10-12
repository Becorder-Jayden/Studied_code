# # 부분집합 → 바이너리 카운팅(비트 연산)

# arr = 'ABC'
# N = len(arr)
# bits = [0]*N    # 원소의 개수만큼 공간을 만듬
# 모든 부분집합은 2^N개 → 2^3 = 8개
# for i in range(2):          # A의 포함 여부(0/1)를 선택
#     bits[0] = i
#     for j in range(2):      # B의 포함 여부를 선택
#         bits[1] = j
#         for k in range(2):  # C의 포함 여부를 선택
#             bits[2] = k
#             # print(bits)
#             # print(i, j, k)

# ===================================================================

# 위 코드를 재귀호출로 변경 시도 ← 트리 모양으로 그릴 수 있기 때문에
def backtrack(k):
    if k == N:
        print(bits)     # 하나의 부분집합에 대해 계산작업

    ''' 아래 코드로 변환
    for i in range(2):
        bits[k] = i
        backtrack(k+1)         # 재귀 호출의 실행
    '''
    i = 0
    bits[k] = 0     # k번 원소를 포함하지 않음
    backtrack(k+1)

    # i = 1
    bits[k] = 1     # k번 원소를 포함
    backtrack(k+1)


backtrack(0)    # 시작 값을 0으로 주고 실행 시작


# ===================================================================
# ===================================================================


# 부분수열의 합 풀이 예시 (with. bits를 사용해서 선택했는지 여부를 확인)

arr = [i for i in range(1, 4+1)]
N = len(arr)
bits = [0] * N

def backtrack(k, cur_sum):      # cur_sum: 0~k-1번 원소중에 포함된 원소들의 합
    if k == N:
        print(bits, end=' ')
        S = 0
        for i in range(N):
            if bits[i] == 1:
                print(arr[i], end=' ')
                S += arr[i]
        print('-->', S, cur_sum)          # ※ bits를 사용해서 확인한 결과값 S와 매개변수 cur_sum을 이용한 결과가 동일한 것을 확인할 수 있다
                                          # 번거로운 bits 메모리 사용을 줄이기 위해 매개변수만을 이용해서 backtrack() 작성 시도
    else:
        # 가지치기의 성능에 따라 bits[k]=0, bits[k]=1의 위치를 변경할 수도 있다
        bits[k] = 1                       # k번 원소를 포함
        backtrack(k+1, cur_sum + arr[k])

        bits[k] = 0                       # k번 원소를 포함 안함
        backtrack(k+1, cur_sum)

backtrack(0, 0)

# bits[k] = 1: k번째 인덱스에 위치한 원소를 '선택'하겠다.
# 트리 상에서 무엇을 선택했는지 확인이 가능하기 때문에 '가치지기'가 가능
# 가치지기의 기준을 매개변수로 사용: 지금까지 어떤 선택을 해왔는지를 확인  ex) cur_sum
# bits 사용안하고 간소화


# ===================================================================


def backtrack(k, cur_sum):
    global ans
    if cur_sum > hap:       # 가지치기: 이미 선택한 값들의 합이 목표치인 hap보다 클 경우
        return
    if k == N:
        if cur_sum == hap:
            ans += 1
    else:
        backtrack(k+1, cur_sum+arr[k])
        backtrack(k+1, cur_sum)

T = int(input())
for tc in range(1, T+1):
    N, hap = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    backtrack(0, 0)
    print(f'#{tc} {ans}')