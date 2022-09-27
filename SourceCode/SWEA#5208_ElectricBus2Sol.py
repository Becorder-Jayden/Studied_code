'''
1. 현재 정류장 번호
2. 충전지 잔량
3. 충전 횟수
정보를 가지고 움직여야 함
'''

import sys
sys.stdin = open('../Solving/input.txt')

# 못풀었다..

def dfs(start):
    global fuel, cnt
    fuel = station[start]       # 해당 역에서 충전 진행
    cnt += 1                    # 교체했을 때, cnt 증가

    if start == len(station):
        return cnt

    if fuel == 0:
        return

    for i in range(1, fuel):
        fuel -= 1
        dfs(start+i)

for tc in range(1, int(input())+1):
    station = list(map(int, input().split()))
    fuel = 0
    cnt = 0
    dfs(0)


    # print(station)
    # print(f'#{tc}')