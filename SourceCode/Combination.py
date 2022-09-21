# 조합(combination): 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것

# 재귀 호출을 이용한 조합 생성 알고리즘
# nCr = n-1Cr-1 + n-1Cr     : 하나의 원소를 포함하는 경우의 수 + 하나의 원소를 제외하는 경우의 수

# 1. 선택: 순열/부분집합/조합
# 2. 행동
# 3. 결과 비교

def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

A= [1,2,3,4,5]
n = len(A)
r = 3
comb = [0] * r
nCr(n, r, 0)