import sys
sys.stdin = open('input.txt')

# 이진탐색을 진행하기 위해 리스트는 오름차순이 되어있어야 한다
# 지표의 사용, break, continue 조금 더 활용하기
# 이진탐색 반복문형, 재귀형 모두 활용할 수 있어야 한다

def BinarySearch(arr, i):
    global cnt

    left = 0
    right = len(arr) - 1

    flag = -1                           # 지표를 사용
    while left <= right:                # 조건내에서 탐색
        mid = (left + right) // 2       # 중앙 값

        if arr[mid] == i:               # 중앙값이 찾는 값이라면
            cnt += 1                    # 조건에 맞는 개수 cnt += 1
            return                          #
        elif arr[mid] > i:              # 찾는 값이 더 작을 때
            if flag == 0:               # 이미 왼쪽방향을 탐색했다면 중단
                break
            right = mid - 1             # 우측 인덱스 정리
            flag = 0                    # 탐색 방향을 표시
        else:                           # 찾는 값이 더 클 때
            if flag == 1:               # 이미 오른쪽방향을 탐색했다면 중단
                break
            left = mid + 1              # 왼쪽 인덱스 정렬
            flag = 1                    # 탐색 방향을 표시


answer_li = []
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()                            # 기준이 되는 리스트는 정렬이 되어 있어야 함
    cnt = 0
    for i in B:
        BinarySearch(A, i)

    answer_li.append(f'#{tc} {cnt}')
print('\n'.join(answer_li))