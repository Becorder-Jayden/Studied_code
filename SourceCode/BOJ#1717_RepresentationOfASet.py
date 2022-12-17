import sys
sys.stdin = open('BOJ#1717_RepresentationOfASet.txt')
sys.setrecursionlimit(10**5)

# 서로소 집합 문제
# pypy3 채점

def find(x):    # x의 부모 값을 return
    if x == p[x]:       # 자기 자신을 부모로 갖는 경우
        return p[x]     # 그대로 return
        # return x를 해도 동일함, 그러나 return 값을 p[x]로 맞춰주기 위해 p[x]로 연습하자

    # 자기 자신을 부모로 갖지 않는 경우
    p[x] = find(p[x])   # path compression 진행
    return p[x]         # x의 부모 값을 return

def union(x, y):
    # test 1: 257616kb 4996ms
    # p[find(y)] = find(x)    # y값의 부모를 x값의 부모로 변경

    # test 2: 278440kb 5008ms
    # if find(x) < find(y):
    #     p[find(y)] = find(x)
    # else:
    #     p[find(x)] = find(y)

n, m = map(int, input().split())
p = [i for i in range(n+1)]     # p: 부모로 가리키고 있는 값을 나타내는 리스트

for _ in range(m):
    ord, a, b = map(int, input().split())
    if ord == 0:    # a, b의 집합을 하나로 합친다
        union(a, b)
    else:   # ord == 1일 때 합집합 여부 확인
        if find(a) == find(b):  # a의 부모 노드와 b의 부모 노드가 같다 → 같은 집합이다
            print("YES")
        else:
            print("NO")








# def find(x):
#     if x == p[x]:
#         return x
#
#     p[x] = find(p[x])
#     return p[x]
#
# def union(x, y):    # x, y를 통합
#     if find(x) < find(y):
#         p[find(y)] = find(x)
#     else:
#         p[find(x)] = find(y)
#
#
#
# n, m = map(int, input().split())
# p = [i for i in range(n+1)]       # n+1개의 저장공간 생성
#
# for _ in range(m):
#     ord, a, b = map(int, input().split())
#     if ord == 0:
#         union(a, b)     # p[b]를 a으로 변경
#     else:
#         if find(a) == find(b):
#             print('YES')
#         else:
#             print('NO')
#             # print('no', find(a), find(b))
#     print(p)