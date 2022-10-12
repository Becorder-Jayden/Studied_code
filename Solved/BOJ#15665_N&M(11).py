import sys
sys.stdin = open('BOJ#15665_N&M(11).txt')

def perm(level, temp):
    if level == M:
        answer_li.append(tuple(temp))
        return
    for i in range(N):
        perm(level+1, temp+[arr[i]])


N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer_li = []

arr.sort()
visited = [0] * N
perm(0, [])

answer_li = list(set(answer_li))
answer_li.sort()
for i in answer_li:
    print(*i)
