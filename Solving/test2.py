# arr = [1,2,3,4]
# p = [0]*3
# visited = [0]*4
#
# def perm(level, N = 4):
#     print('p',p)
#     if level == N-1:
#         print('이게 결과야:',p)
#         return
#     for i in range(0,N):
#         if visited[i] == True: continue
#         visited[i] = 1
#         p[level] = arr[i]
#         print('p','arr[i]',p,arr[i])
#         perm(level+1)
#         visited[i] = 0
#
# perm(0)


arr = [1,2,3,4]
p = [0]*3
visited = [0]*4

# # 순열을 만들어보자
# def perm(level, N):
#     if level == N-1:
#         print(p)
#         return
#     for i in range(N):
#         if visited[i] == True: continue
#         visited[i] = 1
#         p[level] = arr[i]
#         perm(level+1, N)
#         visited[i] = 0
#
# perm(0, 4)

# # 순열을 만들어보자
# def perm(depth, N):
#     if depth == N-1:
#         print(p)
#         return
#     for i in range(N):
#         if visited[i]: continue
#         visited[i] = 1
#         p[depth] = arr[i]
#         perm(depth+1, N)
#         visited[i] = 0
#
# perm(0, 4)

# 순열을 만들어보자
def perm(depth, N):
    if depth == N:
        print()
        return
    for i in range(N):
        if visited[i]: continue     # 방문되 있을 경우 넘어가
        visited[i] = 1              # 안되있을 겨우 방문 처리하고
        p[depth] = arr[i]           #
        perm(depth+1, N)
        visited[i] = 0

