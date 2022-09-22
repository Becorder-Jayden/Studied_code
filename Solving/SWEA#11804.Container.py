import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_li = sorted(list(map(int, input().split())), reverse=True)
    M_li = sorted(list(map(int, input().split())), reverse=True)
    ans = []

    for i in N_li:
        for j in M_li:
            if M_li == False:
                break
            if j >= i:                  # j >= i값을 찾을 때, ans 리스트에 더해주고, 해당 값을 pop해서 제거
                ans.append(i)
                M_li.pop(0)
                break
    print(f'#{tc} {sum(ans)}')