import sys

N, M = map(int, sys.stdin.readline().split())
D = [[0] * (N+1)]
S = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    D_row = [0] + list(map(int, sys.stdin.readline().split()))
    D.append(D_row)

for col in range(1, N+1):  # 범위를 1~N+1로 설정하고 D를 업데이트 하는 방식이 훨씬 편하다
    for row in range(1, N+1):
        S[col][row] = S[col-1][row] + S[col][row-1] - S[col-1][row-1] + D[col][row]  # 배열 누적 합 구하기 

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])  # S와 D배열 구분 주의


