# 부분집합 구하기
## 설명이 필요: 완벽하게 이해하기 어렵다..

arr = [1,2,3,4,5]
result = []
for i in range(1<<len(arr)):    # 부분집합의 개수 : 2**n
  subset = []                   # 만들어진 부분집합을 담을 공간
  for j in range(len(arr)):
    if i & (1<<j):
      subset.append(arr[j])
  result.append(subset)
print(result)