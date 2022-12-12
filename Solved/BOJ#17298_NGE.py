import sys
sys.stdin = open('BOJ#17298_NGE.txt')

# N의 크기: 1~1,000,000 -> O(n)으로 끝내야?
# stack 구조 활용

N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N   # 기본값으로 -1을 세팅
stack = [0]

# 오른쪽 값이 현재 값보다 작을 때: 스택에 인덱스 값을 push
# 오른쪽 값이 현재 값보다 클 때: 스택에서 값을 pop하면서, 더 큰 값이 나올 때까지, 기준점의 오른쪽 값으로 대체
# 마지막 인덱스의 경우 스택에 쌓인 값이 없으므로 기본값으로 설정한 -1이 그대로 적용
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)


# N = int(input())
# A = list(map(int, input().split()))
# temp = []
# ans_lst = []
#
# for i in range(N-1, -1, -1):
#     if temp == []:
#         ans_lst.append(-1)
#         temp.append(A[i])
#     else:
#         if temp:
#             while A[i] > temp[-1]:
#                 temp.pop()
#             ans_lst.append(temp[-1])
#             temp.append(A[i])
#         else:
#             temp.append(-1)
# print(ans_lst)