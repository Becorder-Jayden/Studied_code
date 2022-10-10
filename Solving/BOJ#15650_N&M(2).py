import sys
sys.stdin = open('BOJ#15650_N&M(2).txt')

def comb(level, start, temp):
    if level == M:
        print(*temp)
        return
    for s in range(start+1, N):
        comb(level+1, s, temp+[s+1])

N, M = map(int, input().split())
comb(0, -1, [])