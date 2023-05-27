N, M = map(int, input().split())
A = list(map(int, input().split()))  # 입력 데이터 배열
S = [0] * N  # 누적합 배열
C = [0] * M  # 같은 나머지 인덱스를 카운트
S[0] = A[0]
answer = 0

# 합 배열 저장
for i in range(1, N):
    S[i] = S[i-1] + A[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1  # 하나의 값을 M으로 나누었을 때 떨어지는 경우
    C[remainder] += 1

# nCr 적용 -> nC2 (구간 합: [from, to]: 요소 2개)
for i in range(M):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)

