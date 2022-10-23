import sys
sys.stdin = open('BOJ#17135_CastleDefence.txt')




## 왼쪽 궁수부터 가능한 곳을 맞추면 다음과 같을 때 오류가 발생
# [1, 0, 1, 0, 1]
# [0, 1, 0, 1, 0]
# [1, 1, 0, 0, 0]
# [0, 0, 0, 1, 1]
# [3, 1, 0, 1, 0]   # 원인 1
# [0, 0, 3, 0, 1]   # 원인 2
# [4, 4, 4, 4, 0]

# 따라서 궁수들이 돌아가며 자신에게 가장 가까운 적부터 공격할 수 있도록 설정해야 함.

# 궁수 배치 케이스마다 arr을 초기화 해줘야 함 how?
# 가까운곳부터 쏴야? 멀리부터 쏴야?
# 문제점: 거리가 가까운 곳부터 모든 궁수를 확인하고 다음 거리를 확인해야 하는데,
# 현재 가까운 곳부터 먼곳까지 한 궁수에 대해 확인하고 다음 궁수로 넘어가고 있음

# 반례 탐색하기 10/21
'''s
5 5 2
1 0 1 1 1
0 1 1 1 1
1 0 1 0 1
1 1 0 1 0
1 0 1 0 1
답 14라고 함 (https://www.acmicpc.net/board/view/73578)
'''

# TIP
## 이차원 배열의 copy 방법: copy_arr = [arr[i][:] for i in range(len(arr))]
## 반례를 찾을 때는 주어진 조건의 max값을 토대로 확인해볼 것

# =============================

# Solution
# 1. Day 적군의 이동 v
# 2. Day 궁수의 공격 v
# 3. 궁수의 배치 - 5칸 중에 3칸을 선택하는 방법: 5C3

from collections import deque

#3 각 위치에서의 궁수, 공격
def archor(r, dist):
    for row in range(M):
        for col in range(N-1, N-2-dist, -1):
            if col < 0: continue                                                     ### 반례 맥시멈으로 찾아보기

            # 적이 있고, 궁수와의 거리가 dist 보다 같거나 적을 때
            if arr[col][row] == 1 or arr[col][row] == 3:
                if (N-col) + abs(row - r) <= dist and arr[-1][r]:
                    global answer
                    if arr[col][row] == 1:
                        arr[col][row] = 3
                        answer += 1
                    arr[-1][r] = 0
                    return

#2 하루동안 적의 움직임
def daily_move(arr):
    queue = deque(arr)
    for d in range(1, D+1):
        for i in range(M):
            if queue[-1][i] == 4:
                archor(i, d)

    for col in range(N):
        for row in range(M):
            if arr[col][row] == 3:
                arr[col][row] = 2

    queue.appendleft([0]*M)
    del queue[-2]

    return queue


#1 궁수의 위치 - 메인 함수
def position(level, start, temp):
    if level == 3:
        global arr, answer
        arr2 = [arr[i][:] for i in range(len(arr))]

        li = [0] * M
        for i in temp:
            li[i] = 4

        for i in range(N):
            arr.append(li[:])
            arr = daily_move(arr)
            arr.pop()

        answer_li.append(answer)
        arr = [arr2[i][:] for i in range(len(arr2))]
        answer = 0
        return

    lst = [i for i in range(M)]
    for s in range(start+1, M):
        position(level+1, s, temp+[lst[s]])



N, M, D = map(int, input().split())     # N: 행의 수, M: 열의 수, D: 궁수 사거리
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
answer_li = []

position(0, -1, [])

print(max(answer_li))
