import sys
sys.stdin = open('BOJ#15686_ChickenDelivery.txt')

# 가지치기로 풀이 시간을 줄이고 싶은데..!
# 테스트 케이스는 모두 맞혔고, 가지치기 시도로 코드 수정하면서 오답이 발생


def comb(level, start, temp):
    if level == M:
        global answer
        ans = 0

        for i in temp:
            cc, cr = chicken_li[i][0], chicken_li[i][1]
            for hc, hr in house_li:
                d[hc][hr] = min(d[hc][hr], abs(cc-hc)+abs(cr-hr))

        for col in range(N):
            for row in range(N):
                if d[col][row] != 0xffffff:
                    ans += d[col][row]
                    if ans > answer:
                        return
                    d[col][row] = 0xffffff

        answer = ans
        return

    for i in range(start+1, len(chicken_li)):
        comb(level+1, i, temp+[i])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [[0xffffff] * N for _ in range(N)]

chicken_li = []
house_li = []

for col in range(N):
    for row in range(N):
        if arr[col][row] == 2:
            chicken_li.append([col, row])
        if arr[col][row] == 1:
            house_li.append([col, row])
            d[col][row] = 0xffffff

answer = 0xffffff

comb(0, -1, [])

print(answer)
