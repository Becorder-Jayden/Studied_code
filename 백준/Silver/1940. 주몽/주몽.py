import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))   # 정렬: O(nlogn), 1<=M<=15000이기 때문에 가능
answer = 0

start_idx = 0
end_idx = N-1
S = arr[start_idx] + arr[end_idx]

while start_idx != end_idx:
    if S < M:
        S -= arr[start_idx]
        start_idx += 1
        S += arr[start_idx]
    
    elif S == M:
        answer += 1

        S -= arr[end_idx]
        end_idx -= 1
        S += arr[end_idx]
    else:
        S -= arr[end_idx]
        end_idx -= 1
        S += arr[end_idx]

print(answer)