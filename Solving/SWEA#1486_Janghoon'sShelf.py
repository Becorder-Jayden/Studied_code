import sys
sys.stdin = open('input.txt')

# 매개변수 자체에 더해가는 값을 변수로 사용하는 것도 좋아보임



# # 부분집합 구하기 함수 적용
# def subset(li):
#     ret = []
#     for i in range(1<<len(li)):         # 부분집합의 개수: 2**n, n == 리스트 원소의 개수
#         subset = []                     # 부분집합의 개수만큼 빈 리스트 공간 생성
#         for j in range(len(li)):
#             if i & (1<<j):
#                 subset.append(li[j])
#         if sum(subset) >= B:            # B보다 S의 합이 클 때에만
#             ret.append(sum(subset))
#     return min(ret)                     # 가능한 부분집합 ret에서 가장 작은 값을 출력
#
#
# T = int(input())
# for t in range(T):
#     N, B = map(int, input().split())
#     clerk = list(map(int, input().split()))
#
#     print(f'#{t+1}', subset(clerk)-B)       # 선반과 S와의 차이 값을 출력


# ==== 재귀를 이용한 조합 만들기 사용 ====

# 부분집합 구하기
def subset(i, k):
    global minV
    if i == k:
        S = 0
        for j in range(k):
            if used[j]:
                S += H_lst[j]
        if S >= B:
            if minV > S:
                minV = S
    else:
        used[i] = 0             # 선택하지 않았을 때
        subset(i+1, k)
        used[i] = 1             # 선택했을 때
        subset(i+1, k)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H_lst = list(map(int, input().split()))
    used = [0]*N
    L = len(H_lst)
    ans_li = []
    minV = 0xffff

    subset(0, L)

    print(f'#{tc} {minV-B}')
