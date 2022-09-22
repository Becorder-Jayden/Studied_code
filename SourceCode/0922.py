'''

# 방법 1      # pick 배열 사용
arr = [1,2,3,4]
N = len(arr)
pick = []
def backtrack(k):
    if len(pick) == 2:
        print(pick)
    if k == N:
        print(pick)
    else:
        pick.append(arr[k])
        backtrack(k+1)      # k번 원소를 포함
        pick.pop()

        backtrack(k+1)      # k번 원소를 배제

backtrack(0)


# 방법 2      # 매개변수 사용
arr = [1,2,3,4]
N = len(arr)
def backtrack(k, lst):
    if len(lst) == 2:
        print(lst)
        return
    if k == N:
        return
    else:
        backtrack(k+1, lst+[arr[k]])      # k번 원소를 포함
        backtrack(k+1, lst)      # k번 원소를 배제

backtrack(0, [])

'''

# 3개를 뽑을 때 조합 생성
arr = [1,2,3,4]
N = len(arr)
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])