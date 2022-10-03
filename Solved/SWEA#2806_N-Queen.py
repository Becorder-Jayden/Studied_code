# 0~n으로 만들 수 있는 수 조합 생성
# 시간을 줄이는 방법 생각

def perm(depth, N, S=0):
    global visited, ans
    if depth == N:
        print(temp)
        return

    for i in range(N):
        if visited & (1 << i): continue
        visited += 1 << i
        temp[depth] = i
        perm(depth+1, N)
        visited -= 1 << i


for tc in range(1, int(input())+1):
    N = int(input())
    visited = 0
    temp = [0] * N
    ans = 0
    perm(0, N, 0)
    print(f'#{tc} {ans}')