import sys
sys.stdin = open('BOJ#15664_N&M(10).txt')

def comb(level, start, temp):
    if level == M:
        answer_li.append(tuple(temp))
        return
    for i in range(start+1, N):
        comb(level+1, i, temp+[arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer_li = []
arr.sort()
comb(0, -1, [])

answer_li = list(set(answer_li))
answer_li.sort()
for i in answer_li:
    print(*i)