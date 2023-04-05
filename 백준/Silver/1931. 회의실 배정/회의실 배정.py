# 제출용_sort a[0] o
# 

import sys

N = int(sys.stdin.readline())
time = []


for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time.append([start, end])

# end 시각을 기준으로 오름차순 정렬
# 이때 시간 복잡도 = O(NlogN)                  # Q. why?
time = sorted(time, key = lambda a : a[0])    # 2차원 요소를 기준으로 정렬할 때 key = lambda a:a[n] 사용
time = sorted(time, key = lambda a : a[1])    # a[1] 정렬을 나중에 해줘야 최종적으로 a[1] 기준이 우선됨

last_end = 0
cnt = 0

for start, end in time:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)