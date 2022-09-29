import sys
sys.stdin = open('../Solving/input.txt')

# 탐색 범위에 대해서 확인 잘 할 것..
# runtim error일 경우 특히 인덱스 범위 잘 살펴볼 것

def exp(player, i):
    global ans
    if player == p1:
        if p1_cnt[li[i]] == 3:
            ans = 1
        else:
            for i in range(10-2):                                   # 오답 수정 : 10-3 → 10-2
                if p1_cnt[i] and p1_cnt[i+1] and p1_cnt[i+2]:
                    ans = 1

    elif player == p2:
        if p2_cnt[li[i]] == 3:
            ans = 2
        else:
            for i in range(10-2):
                if p2_cnt[i] and p2_cnt[i + 1] and p2_cnt[i + 2]:
                    ans = 2

T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    p1, p2 = [], []
    p1_cnt, p2_cnt = [0] * 10, [0] * 10
    ans = 0

    for i in range(len(li)):
        if i % 2 == 0:
            p1.append(li[i])
            p1_cnt[li[i]] += 1
            exp(p1, i)
            if ans == 1:
                break
        else:
            p2.append(li[i])
            p2_cnt[li[i]] += 1
            exp(p2, i)
            if ans == 2:
                break

    print(f'#{tc} {ans}')

