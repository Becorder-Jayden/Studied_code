import sys
sys.stdin = open('BOJ#5430_AC.txt')

# 시간초과 발생 -> 덱 사용?
# 런타임 에러?
from collections import deque

# 2차시 : 33% 시간초과 -> for 문 안에서 reverse()를 사용하면서 O(n^2)이 되기 때문이라 함
T = int(input())
for tc in range(1, T+1):
    p = list(input())
    n = int(input())
    inp = deque(input()[1:-1].split(','))
    err = False
    rcnt = 0
    for i in p:
        if i == 'R':
            rcnt += 1
        elif i == 'D':
            print(len(deque([''])))
            if len(inp) > 0 and inp != deque(['']):     # 여기서 문제가 발생
                if rcnt % 2 == 1:       # 홀수 번 뒤집기가 진행되었을 때
                    inp.pop()
                else:
                    inp.popleft()
            else:
                err = True
                break

    if err:
        print('error')
    else:
        if rcnt % 2 == 0:
            print('[' + ','.join(inp) + ']')
        else:
            inp = list(reversed(inp))
            print('[' + ','.join(inp) + ']')

# 1차시 : 시간초과
# def R():
#     global arr
#     narr = []
#     for i in range(len(arr)):
#         popped = arr.pop()
#         narr.append(popped)
#
#     arr = narr
#
# def D():
#     global arr
#     if len(arr) == 0:
#         return
#     else:
#         arr = arr[1:]
#
# T = int(input())
# for tc in range(1, T+1):
#     p = list(input())
#     n = int(input())
#     inp = deque(input())
#     print(inp)
#
#     for i in p:
#         if i == 'R':
#             R()
#         else:
#             D()
#
#     ans = 'error'
#     if arr:
#         ans = '['
#         ans += ','.join(arr)
#         ans += ']'
#     print(ans)
