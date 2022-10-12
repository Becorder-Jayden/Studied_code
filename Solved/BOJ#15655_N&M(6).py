import sys
sys.stdin = open('BOJ#15655_N&M(6).txt')

# 조합 생성할 때 start 지표 잊지 말기
# start: 범위 탐색할 때 시작점을 의미

def comb(lev, start, tmp):
    if lev == M:
        print(*tmp)
        return

    for i in range(start, N):
        comb(lev+1, i+1, tmp+[arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * N
arr.sort()
comb(0, 0, [])
