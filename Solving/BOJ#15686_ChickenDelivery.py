import sys
sys.stdin = open('BOJ#15686_ChickenDelivery.txt')

# 치킨집이 p개, 제한된 수가 m개일 때 조합 -> p개에서 m개를 뽑을 때 조합
def dfs(p, m):
    pass


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [[0xfff] * N for _ in range(N)]

chicken_li = []
house_li = []
for col in range(N):
    for row in range(N):
        if arr[col][row] == 2:
            chicken_li.append((col, row))
        if arr[col][row] == 1:
            house_li.append((col, row))

for cc, cr in chicken_li:
    for hc, hr in house_li:
        dist = abs(cc-hc) + abs(cr-hr)
        if dist < d[hc][hr]:
            d[hc][hr] = dist


ans = 0
for col in range(N):
    for row in range(N):
        if d[col][row] < 0xfff:
            ans += d[col][row]

print('ans:', ans)

for i in d:
    print(*i)

# print('chicken_li:', chicken_li)
# print('house_li:', house_li)

# n개를 선택하는 경우를 조합으로 만들어서 chicken 리스트에서 조합을 만들고 값을 비교..