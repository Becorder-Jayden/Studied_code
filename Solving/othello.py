import sys
sys.stdin = open('othello.txt')

dcol = [-1, 1, 0, 0]
drow = [0, 0, -1, 1]


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2, 2
    arr[N//2][N//2-1], arr[N//2-1][N//2] = 1, 1


    for i in arr:
        print(i)
