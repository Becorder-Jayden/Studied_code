import sys
sys.stdin = open('BOJ#9663_N-Queen.txt')

# 백트래킹으로 모든 경우의 수 탐색

## 구글링 코드
## 시간초과가 너무 까다로운 문제였다 -> 실제로 스스로 풀지 못함
## check 함수를 통해서 T

def check(x):           # 이전 열에 겹치는 행이 있는 지 체크
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x-i:     # 같은 열에 말이 놓였거나, 대각선에 위치할 경우
            return False    # n-queen 조건에 부합하지 않음
    return True

def dfs(x):
    global cnt

    if x == N:              # 최대 깊이에 도닥했을 경우에
        cnt += 1            # cnt 개수를 추가
        return

    for i in range(N):
        if visited[i]: continue     # 이미 방문했던 곳이라면 넘어가기
        rows[x] = i
        print('rows:', rows)
        if check(x):
            visited[i] = True       # 방문표시
            dfs(x+1)
            visited[i] = False      # 방문표시 제거

N = int(input())
rows = [0] * N
visited = [False] * N           # 시간초과 문제 해결을 위해 visited 처리
cnt = 0

dfs(0)
print(cnt)





## 시간 초과
# def exp(level, idx):
#     global lst, ans
#
#     print(level)
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i][0] == lst[j][0] or lst[i][1] == lst[j][1] or abs(lst[j][0]-lst[i][0]) == abs(lst[j][1]-lst[i][1]):
#                 return
#
#     if level == N:
#         ans += 1
#         return
#
#     for i in range(N):
#         lst.append((level, i))
#         exp(level+1, i)
#         lst.pop()
#
# N = int(input())
# lst = []
# ans = 0
# exp(0, 0)
#
# print('ans:', ans)





## 시간 초과
# def exp(level, idx):
#     global lst, ans
#
#     if level == N:
#         for i in range(N):
#             for j in range(i+1, N):
#                 if lst[i][0] == lst[j][0] or lst[i][1] == lst[j][1] or abs(lst[j][0]-lst[i][0]) == abs(lst[j][1]-lst[i][1]):
#                     return
#         ans += 1
#         return
#
#     for i in range(N):
#         lst.append((level, i))
#         exp(level+1, i)
#         lst.pop()
#
# N = int(input())
# lst = []
# ans = 0
# exp(0, 0)
#
# print('ans: ', ans)