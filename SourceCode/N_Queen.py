'''
n-Queen 교수님 풀이
* 같은 행, 열에 두면 안됨 → 순열을 활용할 수 있다.
* 0부터 n-1값을 순서대로 나열
* 이전에 놓여진 퀸들의 위치에 영향을 받는지를 체크, 영향을 받으면 가지치기, 받지 않으면 선택
1. 대각 = 기울기가 1, 행값의 차이/열값의 차이 = 1
대각 라인을 확인했을 때 어떤 라인에 있는지 확인
대각 라인의 개수 : 2N-1, 행 기준 확인(N) 후 열 기준 확인(N-1)
(r,c)를 통해 어느 대각선에 위치했는지 확인할 수 있음 : r+c
어렵게 생각하지 말고 2N개 정도를 만들면 됨, 그리고 방문 표시
반대의 대각(역대각) : r-c+(N-1)
'''

# def nQueen(row, visit):
#     if row == N:
#         global ans
#         ans += 1
#     else:
#         for col in range(N):
#             if visit & (1 << col): continue         # 지금 방문하려고 하는 열이 이미 방문 되어 있다면 건너뜀, 같은 열은 제외
#             # 같은행, 같은 열은 제외
#             a = row + col
#             b = row - col + (N-1)
#
#             # 대각에 대해서 체크
#             if Line1[a] or Line2[b]: continue       # 대각의 값이 이미 존재한다면(방문한 적이 있는 대각이라면(
#             Line1[a] = Line2[b] = 1
#             nQueen(row+1, visit | (1 << col))
#             Line1[a] = Line2[b] = 0


def nQueen(row):
    if row == N:
        global ans
        ans += 1
    else:
        for col in range(N):
            if visit[col]: continue         # 지금 방문하려고 하는 열이 이미 방문 되어 있다면 건너뜀, 같은 열은 제외
            # 같은행, 같은 열은 제외
            a = row + col
            b = row - col + (N-1)

            # 대각에 대해서 체크
            if Line1[a] or Line2[b]: continue       # 대각의 값이 이미 존재한다면(방문한 적이 있는 대각이라면(
            visit[col] = Line1[a] = Line2[b] = 1
            nQueen(row+1)
            visit[col] = Line1[a] = Line2[b] = 0


for i in range(1, 11):
    N = i               # N = i 일때
    ans = 0
    visit = [0] * N
    Line1 = [0] * (N+N)     # ↗: row + col
    Line2 = [0] * (N+N)     # ↘: row - col + (N-1)
    nQueen(0)
    print(f'{i}Queen: {ans}개')