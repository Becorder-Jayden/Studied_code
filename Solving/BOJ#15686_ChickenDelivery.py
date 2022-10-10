import sys

sys.stdin = open('BOJ#15686_ChickenDelivery.txt')


# 순열(visited) 조합(visited x) 부분집합(powerset)

# 치킨집이 p개, 제한된 수가 m개일 때 조합 -> p개에서 m개를 뽑을 때 조합
# def perm(depth, N):
#     global visited
#     if depth == N:
#         print(temp)
#         return
#
#     for i in range(N):
#         if visited & (1 << i): continue
#         visited += 1 << i
#         temp[depth] = i
#         perm(depth + 1, N)
#         visited -= 1 << i


# def perm(start, m):
#     global answer_li
#     for i in range(chick_len):
#
        # for j in range(i+1, chick_len):

            # print((i, j))
            # for cc, cr in [chicken_li[i], chicken_li[j]]:
            #     for hc, hr in house_li:
            #         dist = abs(cc - hc) + abs(cr - hr)
            #         if dist < d[hc][hr]:
            #             d[hc][hr] = dist
            #
            # total_dist = 0
            # for col in range(N):
            #     for row in range(N):
            #         if d[col][row] != 0xfff:
            #             total_dist += d[col][row]
            #             d[col][row] = 0xfff
            # answer_li.append(total_dist)

def dfs(depth, N, idx):
    if depth == N:
        print(temp)
        return
    for i in range(idx, len(chicken_li)):
        if visited[i] == 0:
            visited[i] = 1
            temp[depth] = p[i]
            dfs(depth+1, N, i)
            visited[i] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [[0xfff] * N for _ in range(N)]

chicken_li = []
house_li = []
for col in range(N):
    for row in range(N):
        if arr[col][row] == 2:
            chicken_li.append([col, row])
            d[col][row] = 0xfff
        if arr[col][row] == 1:
            house_li.append([col, row])
            d[col][row] = 1
            d[col][row] = 0xfff

chick_len = len(chicken_li)

temp = [0] * M
p = [i for i in range(len(chicken_li))]
visited = [0] * len(chicken_li)
for i in range(len(p)):
    dfs(0, M, i)

print('chicken_li:', chicken_li)
print('house_li:', house_li)

# n개를 선택하는 경우를 조합으로 만들어서 chicken 리스트에서 조합을 만들고 값을 비교..
# for i in d:
#     print(i)