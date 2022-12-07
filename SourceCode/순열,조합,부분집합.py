# == try myself ==
def comb(level, start, temp):
    if level == 3:
        print(temp)
        return

    for s in range(start+1, 8):
        comb(level+1, s, temp+[arr[s]])

# arr = [i for i in range(8)]
# comb(0, -1, [])

# 조합의 경우 오름차순으로 정렬된 리스트 중에서 이후의 범위만 대상으로 함


def perm(level, temp):
    global visited
    if level == 3:
        print(temp)
        return

    for i in range(8):
        if visited & (1<<i): continue
        visited += 1 << i
        perm(level+1, temp+[arr[i]])
        visited -= 1 << i

arr = [i for i in range(8)]
visited = 0
perm(0, [])

# 순열은 arr 리스트 전범위를 대상으로 함, 이미 선택된 원소를 구분하기 위해 visited 사용
# 비트연산자, visited 리스트, if not in ~, append & pop 등 자기 스타일에 따라 코드형태가 달라지곤 함


def subset(level, temp):
    if level == 3:
        print(temp)
        return

    subset(level+1, temp)
    subset(level+1, temp+[arr[level]])

arr = [i for i in range(8)]
# subset(0, [])









# ============= 빛수민 교수님의's 설명 ============

def comb(level,start,temp): # level : 내가 몇 개 뽑겠다. start : 내가 직전에 이거 뽑았어, temp: 조합
    if level == 3:
        print(temp)
        return
    for i in range(start+1, 7):
        comb(level+1, i, temp+[arr[i]])

def perm(level,temp):
    if level == 3:
        print(temp)
        return
    for i in range(0,7):
        # if arr[i] in temp:            # 전에 뽑았던 거면 뽑지 마라
        if visited[i] == True:
            continue
        visited[i] = True
        perm(level+1, temp+[arr[i]])
        visited[i] = False

def sub_set(level,temp):  # 집합의 원소의 개수
    if level == 3:
        print(temp)
        return
    sub_set(level+1, temp)
    sub_set(level+1, temp+[arr[level]])


# visited = [False]*7

# arr = [1,2,3,4,5,6,7]
# arr = [1,2,3]

# comb(0,-1,[])
# perm(0,[])
# sub_set(0,[])



