# 9/21 Live 강의
'''
5
123123
124467
333444
444456
123444
'''

def BabyGin1(i, k):
    if i == k:
        run = 0
        tri  =0
        if card[0]==card[1] and card[1]==card[2]:
            tri += 1
        if card[0]+1==card[1] and card[1]+card[2]:
            run += 1
        if card[3]==card[4] and card[4]==card[5]:
            tri += 1
        if card[3]+1==card[4] and card[4]+1==card[5]:
            run += 1
        if tri+run == 2:
            return 1
        else:
            return 0
        # print(card)
    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            if BabyGin1(i+1, k):
                return 1
            card[i], card[j] = card[j], card[i]
        return 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    ans = BabyGin1(0, 6)
    if ans:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')


# cnt 배열 사용

T = int(input())
for tc in range(1, T+1):
    card = int(input())
    c = [0]*12

    i = 0
    while i < 6:
        c[card%10] += 1
        card //= 10
        i += 1

    tri = 0
    run = 0
    i = 1

    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1
    if run+tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')