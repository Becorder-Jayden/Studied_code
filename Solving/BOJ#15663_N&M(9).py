import sys
sys.stdin = open('BOJ#15663_N&M(9).txt')

def perm(level, temp):
    if level == M:
        global answer_li
        answer_li.append(tuple(temp))
        return

    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        perm(level+1, temp+[arr[i]])
        visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer_li = []

arr.sort()
visited = [0] * N
perm(0, [])

li = list(set(answer_li))
li.sort()
for i in li:
    print(*i)