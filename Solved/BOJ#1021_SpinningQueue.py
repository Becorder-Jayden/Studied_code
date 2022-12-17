import sys
sys.stdin = open("BOJ#1021_SpinningQueue.txt")

# 1. 첫번째 원소 뽑아내기
# 2. 왼쪽으로 한 칸 이동
# 3. 오른쪽으로 한 칸 이동

from collections import deque

def pop_idx0():
    lst.popleft()
    queue.popleft()
    return

def move_left():
    global exe
    queue.append(queue.popleft())
    exe += 1
    return

def move_right():
    global exe
    queue.appendleft(queue.pop())
    exe += 1
    return


N, M = map(int, input().split())
lst = deque(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
idx = 0
diff = 1
exe = 0

while lst:
    # lst[0]이 queue[0]과 같은지 확인
    if lst[0] == queue[0]:
        pop_idx0()

    # lst[0]이 queue[0]과 다를 때 왼쪽/오른쪽 비교
    else:
        while queue[-diff] != lst[0] and queue[diff] != lst[0]:
            diff += 1
        if queue[-diff] == lst[0]:
            # print('왼쪽으로 이동', diff)
            for i in range(diff):
                move_right()
        elif queue[diff] == lst[0]:
            # print('오른쪽으로 이동', diff)
            for i in range(diff):
                move_left()
        diff = 1
print(exe)