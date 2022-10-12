import sys
sys.stdin = open('BOJ#15657_N&M(8).txt')

def comb(level, start, temp):
    if level == M:
        print(*temp)
        return

    for i in range(start, N):
        comb(level+1, i, temp+[arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
comb(0, 0, [])