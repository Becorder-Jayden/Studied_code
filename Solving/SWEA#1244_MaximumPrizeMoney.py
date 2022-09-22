import sys
sys.stdin = open('input.txt')

# 아직 못품 /////

def exp(k):
    global ans
    if k == L:
        ans = max(ans, int(''.join(map(str, li))))
        print(ans)
    else:
        for i in range(L-1):
            for j in range(i+1, L):
                li[i], li[j] = li[j], li[i]
                exp(k+1, li)
                li[i], li[j] = li[j], li[i]


T = int(input())
for tc in range(1, T+1):
    inp, change = input().split()
    L = len(inp)
    li = []
    for i in inp:
        li.append(int(i))

    ans = 0
    exp(0)
