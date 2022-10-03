import sys
sys.stdin = open('../Solving/input.txt')

# 스스로 다시 풀어볼 것
# 도영코드 기반 + 교수님 해설


def dfs(month, pay):
    global min_money

    if month >= 12:
        if min_money > pay:         # 계산한 비용보다 (예상)최소비용 더 클 경우
            min_money = pay         # 지불 최소비용을 계산한 비용으로 바꿈
        return

    if min_money < pay:             # 계산과정에서 최소비용으로 예상하는 값보다 큰 값이 계산되고 있을 때
        return                      # 가지치기 진행


    if plan[month]:                          # 이용일이 있을 때
        dfs(month+1, pay + plan[month]*d)           # case1) 1일 이용권
        dfs(month+1, pay + m)                       # case2) 1달 이용권
        dfs(month+3, pay + tm)                      # case3) 3달 이용권         # index error 주의 #
    else:
        dfs(month+1, pay)                    # 이용일이 없을 때

for tc in range(1, int(input())+1):
    d, m, tm, y = map(int, input().split())
    plan = list(map(int, input().split()))
    min_money = y
    dfs(0, 0)
    print(f'#{tc} {min_money}')
