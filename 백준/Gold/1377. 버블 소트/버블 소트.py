import sys

N = int(sys.stdin.readline())
arr = []
diff_arr = []
Max = 0
answer = 0

# 입력값 (idx, val)을 arr에 기록
for i in range(N):
    arr.append((i, int(input())))

# val을 기준으로 정렬
sorted_arr = sorted(arr, key = lambda x: x[1])

# 인덱스 차이값을 계산, 최댓값을 구함
for i in range(N):
    diff_idx = sorted_arr[i][0] - arr[i][0]
    diff_arr.append(diff_idx)
    if Max < diff_idx:
        Max = diff_idx

# 정답: 가장 왼쪽으로 많이 이동한 값 + 1 (추가적인 for문이 1번 실행되고 break 진행)
answer = Max+1
print(answer)
