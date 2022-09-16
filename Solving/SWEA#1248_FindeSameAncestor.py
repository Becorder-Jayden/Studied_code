import sys
sys.stdin = open('input.txt')

# 9/16 풀이 완료
# 진행 상황 : 10번 테스트 케이스 오답만 해결하면 됨
# cnt_list를 구성하면서 2가 만들어지는 즉시 break, 해당 값을 기준으로 정답 출력 → 오류 해결

def treeSize(v):
    global cnt
    if v == 0:
        return 0
    l = treeSize(L[v])
    r = treeSize(R[v])
    return l + r + 1

def checkAnc(C):
    global root_cnt
    parent = P[C]
    while True:
        if parent == 1:
            return
        if C in L:
            parent = L.index(C)
            root_cnt[parent] += 1
        elif C in R:
            parent = R.index(C)
            root_cnt[parent] += 1

        if root_cnt[parent] == 2:
            return root_cnt[parent]
        C = parent

T = int(input())
for t in range(T):
    M, E, C1, C2 = map(int, input().split())
    P = [i for i in range(M+1)]
    L = [0] * (M+1)
    R = [0] * (M+1)
    root_cnt = [0] * (M+1)
    inp = list(map(int, input().split()))
    for i in range(0, len(inp), 2):
        p, c = inp[i], inp[i+1]
        if L[p]:
            R[p] = c
        else:
            L[p] = c

    cnt = 0
    checkAnc(C1)
    checkAnc(C2)

    m = 0
    maxIdx = 0
    for i in range(len(root_cnt)):
        if m <= root_cnt[i]:
            m = root_cnt[i]
            maxIdx = i

    print(f'#{t+1} {maxIdx} {treeSize(maxIdx)}')

