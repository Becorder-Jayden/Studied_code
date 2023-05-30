import sys
sys.stdin = open('BOJ#1253.txt')

def check_good_number(i):
    global good_number

    start_idx = 0
    end_idx = i-1
    S = arr[start_idx] + arr[end_idx]

    while start_idx != end_idx:
        if S > arr[i]:
            end_idx -= 1
        elif S < arr[i]:
            start_idx += 1
        else:
            good_number += 1
            end_idx -= 1



N = int(input())
arr = sorted(list(map(int, input().split())))
good_number = 0


for i in range(N):
    check_good_number(i)
    print(i)

print(arr)

print(good_number)