# p = []          # 데이터가 저장된 배열
# k, n = 0, 0     # k:원소의 개수, n: 선택된 원소의 수

# Youtube Live

def permutation(i, k):
    if i == k:          # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]     # 자리를 바꿈
            permutation(i+1, k)
            p[i], p[j] = p[j], p[i]     # 원상 복귀를 위한 자리 바꿈


p = [i for i in range(1, 11)]
# permutation(0, len(p))





# npr3 ========================== 정리 미완료
def npr3(i, k, r):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j]가 사용됨으로 표시
                p[i] = a[j]         # p[i]는 a[j]로 결정
                npr3(i+1, k, r)        # p[i+1] 값을 결정하러 이동
                used[j] = 0

N = 5
R = 5
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * R
p[0] = 1            #
used[0] = 1         #
npr3(1, N, R)       #


# npr4 ============================
def npr4(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                npr4(i+1, k, r)
                used[j] = 0

N = 3
R = 3
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * R
# npr4(0, N, R)






# ================= 웹 코칭 =================
# 순열 생성 → n개에서 r개를 선택해서 순서대로 나열
# r개를 하나씩 n개에서 선택하면 순열을 생성


arr = 'ABC'     # 3개에서 2개를 선택해서 나열
N = len(arr)
pick = [0]*N

for i in range(N):              # 첫번째 요소를 선택
    for j in range(N):          # 두번째 요소를 선택
        if i == j: continue
        for k in range(N):      # 세번째 요소를 선택
            if k == i or k == j: continue
            # print(arr[i], arr[j], arr[k])

def backtrack(k):
    if k == N:              # 기준값(k)이 일정값(N)에 다다르면, 중단
        pass
    for i in range(N):
        if arr[i] in pick: continue
        pick.append(arr[i])
        backtrack(k+1)      # 재귀적 호출할 때 기준값+1
        pick.pop()
backtrack(0)            # 보통은 시작 기준을 변수로 주고 시작


# ===============================

arr = 'ABC'     # 3개에서 2개를 선택해서 나열
N = len(arr)
pick = []


for i in range(N):              # 첫번째 요소를 선택
    if arr[i] in pick: continue
    pick.append(arr[i])
    for j in range(N):          # 두번째 요소를 선택
        if arr[j] in pick: continue
        pick.append(arr[j])
        for k in range(N):      # 세번째 요소를 선택
            if arr[k] in pick: continue
            pick.append(arr[k])
            print(pick)
            pick.pop()
        pick.pop()
    pick.pop()



# 위 코드의 경우 리스트에 넣었다 뺏다가 하는 방법
# 메모리를 적게 쓰고 교체하는 아래 방식을 더 자주 사용

arr = 'ABC'
N = len(arr)
pick = [0] * N
used = [0] * N              # 체크를 위한 메모리 사용

for i in range(N):
    if used[i]: continue
    used[i] = 1
    pick[0] = arr[i]
    for j in range(N):
        if used[j]: continue
        used[j] = 1
        pick[1] = arr[j]
        print(*pick[:2])
        used[j] = 0
    used[i] = 0

