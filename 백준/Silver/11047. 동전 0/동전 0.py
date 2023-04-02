N, K = map(int, input().split())
lst = []
answer = 0
cnt = 0

# 내림차순으로 정렬된 데이터셋 구성
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)

for i in lst:
    cnt = 0
    if K - i >= 0:
        cnt += K//i
        K -= cnt * i
        answer += cnt


print(answer)