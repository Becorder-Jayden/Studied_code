import sys
sys.stdin = open('SWEA#1767_ConnectProcessor.txt')

dcol = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pc_lst = []

    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:
                pc_lst.append((col,row))

    print(pc_lst)