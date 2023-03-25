N = int(input())
lst = list(map(int, input().split()))
stack = []
ans = [0] * N


for i in range(N):
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

print(*ans)