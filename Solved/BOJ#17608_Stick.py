import sys
sys.stdin = open('BOJ#17608_Stick.txt')

N = int(sys.stdin.readline())    # 2 <= N <= 100,000
lst = []
for _ in range(N):
    h = int(input())
    lst.append(h)

top = 0
ans = 0
for i in range(N-1, -1, -1):
    if top < lst[i]:
        ans += 1
        top = lst[i]
print(ans)

# 시간초과
# N = int(input())    # 2 <= N <= 100,000
# lst = [0]
# top = 0
# for _ in range(N):
#     h = int(input())
#     while lst and lst[-1] <= h:
#         lst.pop()
#     lst.append(h)
# print(len(lst))