
import sys
sys.stdin = open('test2.txt')

def day(num_day):
    global balance
    temp = []
    for col in range(N):
        if drr[col][num_day] > 0:
            temp.append((drr[col][num_day], arr[col][num_day], (col, num_day)))
    temp.sort(reverse=True)

    for i in temp:
        if balance > i[1]:
            stock[i[2][0]] += balance // i[1]
            balance = balance % i[1]
    return

def dayout(num_day):
    global balance

    for i in range(N):
        while stock[i]:
            balance += arr[i][num_day]
            stock[i] -= 1
    return

T = int(input())
for tc in range(1, T+1):
    Ms, Ma = map(int, input().split())      # Ms: 예치금, Ma: 월별 불입금액
    N, L = map(int, input().split())        # N: 종목 수, L: 기간
    stock = [0 for _ in range(N)]

    arr = [list(map(int, input().split())) for _ in range(N)]
    drr = []
    for n in range(N):
        temp = []
        for i in range(L):
            temp.append(arr[n][i+1]-arr[n][i])
        drr.append(temp)


    balance = Ms

    for i in range(L):
        day(i)
        balance += Ma
        dayout(i+1)

    revenue = balance - (Ms + Ma*L)
    print(f'#{tc} {revenue}')