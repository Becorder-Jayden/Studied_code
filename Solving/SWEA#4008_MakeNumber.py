import sys
sys.stdin = open('input.txt')

## 아직 못품 !!!
## 지지부진.. 중단..
from collections import deque

# 연산자의 조합 만들기
def perm(depth, N, S=0):
    global visited, ans
    if depth == N:
        print(temp)
        return

    for i in range(N):
        if visited & (1 << i): continue
        visited += 1 << i
        temp[depth] = i
        perm(depth+1, N)
        visited -= 1 << i


for tc in range(1, int(input())+1):
    N = int(input())
    cals = list(map(int, input().split()))
    calculs = []
    for i in range(4):
        while cals[i] > 0:
            calculs.append(i)
            cals[i] -= 1
    nums = list(map(int, input().split()))
    visited = 0          # visit 처리
    temp = [0] * N
    perm(0, 4)
    print()




    # print(N)
    # print(cals)
    # print(calculs)
    # print(nums)
    # perm(0, N, [])