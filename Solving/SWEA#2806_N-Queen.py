import sys
sys.stdin = open('input.txt')

dcol = [1, 1, -1, -1]
drow = [1, -1, 1, -1]

for tc in range(1, int(input())+1):
    arr = [[0]*8 for _ in range(8)]
    for i in arr:
        print(*i)
    print(f'#{tc}')