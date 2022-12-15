import sys
sys.stdin = open('BOJ#1987_Alphabet.txt')

'''
1 1 
A
'''

# dfs 풀이는 pypy3로 제출해야 한다고 함
# 문제 채점 과정이 매우 오래 걸린다
# 정답
# U,R,D,L
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def dfs(col, row):
    global level, max_level
    visited[col][row] = 1   # 방문 처리
    alpha_lst[ord(arr[col][row])-65] = 1    # 방문한 지점의 알파벳 처리
    level += 1  # 재귀가 반복될 때마다 깊이(level) 증가
    max_level = max(level, max_level)   # max 처리를 이곳에서 했더니 오류가 발생하지 않음
    for v in range(4):
        ncol = col + dcol[v]
        nrow = row + drow[v]
        if 0<=ncol<R and 0<=nrow<C and visited[ncol][nrow] == 0 and alpha_lst[ord(arr[ncol][nrow])-65] == 0:
            dfs(ncol, nrow)
            # 재귀의 return 후 기록한 값을 초기화
            visited[ncol][nrow] = 0
            level -= 1
            alpha_lst[ord(arr[ncol][nrow])-65] = 0

R, C = map(int, input().split())    # R: 세로, C: 가로
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
alpha_lst = [0] * 26
level, max_level = 0, 0

dfs(0, 0)

if max_level == 0:
    max_level = 1

print(max_level)

# 오답
# # U,R,D,L
# dcol = [-1, 0, 1, 0]
# drow = [0, 1, 0, -1]
#
# def dfs(col, row):
#     global level, max_level
#     visited[col][row] = 1   # 방문 처리
#     alpha_lst[ord(arr[col][row])-65] = 1    # 방문한 지점의 알파벳 처리
#     level += 1
#     max_level = max(level, max_level)
#     for v in range(4):
#         ncol = col + dcol[v]
#         nrow = row + drow[v]
#         if 0<=ncol<R and 0<=nrow<C and visited[ncol][nrow] == 0:
#             if alpha_lst[ord(arr[ncol][nrow])-65] == 0:
#                 dfs(ncol, nrow)
#                 visited[ncol][nrow] = 0
#                 level -= 1
#                 alpha_lst[ord(arr[ncol][nrow])-65] = 0
#             # else:
#                 # max_level = max(level, max_level)
#                 # return
#
# R, C = map(int, input().split())    # R: 세로, C: 가로
# arr = [list(input()) for _ in range(R)]
# visited = [[0] * C for _ in range(R)]
# alpha_lst = [0] * 26
# level, max_level = 0, 0
#
# dfs(0, 0)
#
# if max_level == 0:
#     max_level = 1
#
# print(max_level)

