# # 순열로 조합가능한 집합 만들기
# def perm(depth, N, S=0):
#     global visited, ans
#     if depth == N:
#         print(temp)
#         return
#
#     for i in range(N):
#         if visited & (1 << i): continue
#         visited += 1 << i
#         temp[depth] = i
#         perm(depth+1, N)
#         visited -= 1 << i
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     visited = 0
#     temp = [0] * N
#     ans = 0
#     perm(0, N, 0)




# # grouping
# 2그룹으로 나누고 싶다
N = 6
arr = [i for i in range(N)]

def backtrack(k):
    if len(A) == N//2:
        print(A, B + arr[k:])
        return
    if len(B) == N//2:
        print(B, A + arr[k:])
        return
    A.append(arr[k])
    backtrack(k+1)
    A.pop()

    B.append(arr[k])
    backtrack(k+1)
    B.pop()

A, B = [arr[0]], []
backtrack(1)

