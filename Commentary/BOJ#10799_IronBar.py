import sys
sys.stdin = open("BOJ#10799_IronBar.txt")

# 스택
# 모든 경우대로 조건문을 나열

arr = list(input())
stack = []
cnt = 0
for i in range(len(arr)):
    if len(stack) == 0 and arr[i] == '(':   # stack이 아직 만들어지지 않았을 경우
        stack.append('(')
    else:   # stack이 존재할 때
        # 이전에 들어온 값과 현재 입력되는 값을 비교
        # 모든 경우의 수는 4가지 밖에 되지 않음
        if arr[i-1] == '(' and arr[i] == '(':       # case1
            stack.append('(')
        elif arr[i-1] == '(' and arr[i] == ')':     # case2
            stack.pop()
            cnt += len(stack)
        elif arr[i-1] == ')' and arr[i] == ')':     # case3
            cnt += 1
            stack.pop()
        else:   # arr[i-1] == ')' and arr[i] = '('  # case4
            stack.append('(')
print(cnt)


# # 첫번째 시도 -> 오류
# arr = list(input())
# stack = []
# cnt = 0
# for i in arr:
#     if i == '(':
#         stack.append('(')
#     else:
#         stack.pop()
#         cnt += len(stack)
#     print(stack, cnt)
# print(cnt)