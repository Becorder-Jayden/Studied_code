N = int(input())
N_arr = sorted(list(map(int, input().split())))
M = int(input())
M_arr = list(map(int, input().split()))

def find(v):
    left, right, mid = 0, len(N_arr)-1, len(N_arr)//2
    while left <= right:    # left, right가 정의된 범위 내에서 탐색이 진행되도록 함
        mid = (left+right)//2       # mid는 탐색이 진행될 때마다 새롭게 정의해서 사용

        # 경우의 수 구분
        if v < N_arr[mid]:
            right = mid - 1
        elif v > N_arr[mid]:
            left = mid + 1
        elif v == N_arr[mid]:
            print(1)
            return
    print(0)

for i in M_arr:
    find(i)
