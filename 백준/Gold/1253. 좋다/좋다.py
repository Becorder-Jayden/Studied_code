import sys

def find_good(i):
    global answer
    start, end = 0, N-1

    while start < end:
        if arr[start] + arr[end] == arr[i]:
            if start != i and end != i:
                answer += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif arr[start] + arr[end] > arr[i]:
            end -= 1
        elif arr[start] + arr[end] < arr[i]:
            start += 1

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0

for i in range(N):
    find_good(i)

print(answer)