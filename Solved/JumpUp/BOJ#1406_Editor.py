import sys
sys.stdin = open('BOJ#1406_Editor.txt')

# 자료구조: 2개의 스택 사용

# pypy3 채점으로 정답
# 스택을 하나 더 사용하는 방식을 사용했다
#   -> popleft() 구조를 사용하지 않아도 된다

left = list(input())
right = []           # 임시 스택 공간
N = len(left)
M = int(input())
for m in range(M):
    ord = list(input().split())

    if ord[0] == 'L':               # 커서 왼쪽 이동
        if left:                         # inp이 존재할 때
            right.append(left.pop())      # right 공간에 저장
    elif ord[0] == 'D':             # 커서 오른쪽 이동
        if right:                        # temp가 존재할 때
            left.append(right.pop())      # temp에서 가져와 다시 저장
    elif ord[0] == 'B':             # 커서 왼쪽 문자 삭제
        if left:
            left.pop()
    else:                           # ord[1] 문자 추가
        left.append(ord[1])

# 모든 ord가 종료되면 temp에 저장된 문자를 가져와 다시 저장
left.extend(reversed(right))
print(''.join(left))




# 시간초과
# inp = list(input())
# N = len(inp)    # 문자열의 길이
# M = int(input())    # 명령어의 개수
# cursor = N      # 커서의 위치
# for m in range(M):
#     ord = input().split()
#     for i in ord:
#         if i == 'L' and cursor >= 1:
#             cursor -= 1
#         elif i == 'D' and cursor < N:
#             cursor += 1
#         elif i == 'P':
#             inp.insert(cursor, ord[1])    # insert(loc, val)
#             cursor += 1
#         elif i == 'B' and not(cursor == 0 and len(inp) == 1):
#             if cursor-1 >= 0:
#                 del inp[cursor-1]
#                 if cursor >= 1:
#                     cursor -= 1
# print(''.join(inp))