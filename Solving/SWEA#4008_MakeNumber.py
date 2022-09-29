import sys
sys.stdin = open('input.txt')

## 아직 못품 !!!


# 연산자의 조합 만들기
def perm(depth, N):
    if depth == N:
        return
    for i in range(N+1):
        print(i)

perm(0, 4)

