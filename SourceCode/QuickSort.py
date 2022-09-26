# 퀵정렬 : 주어진 리스트를 두 개로 분할하고, 각각을 정렬
# 병합정렬과 동일해 보이지만 다른 점을 가짐
'''
- 병합정렬
* 두 부분으로 나누어 진행
* 각 부분 정렬이 끝난 후, 병합하는 '후처리 작업' 필요

- 퀵정렬
* 퀵 정렬은 기준(pivot)을 중심으로 작은 것은 왼쪽, 큰 것은 오른쪽에 위치
* 후처리 작업 불필요
'''


# Hoare_partition 알고리즘 이용
def partition(l, r):
    pivot = A[l]                        # 분할할 범위의 시작값을 pivot으로 설정
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:         # 피봇보다 작거나 같은 값일 때, i를 증가(이동)
            i += 1
        while i <= j and A[j] >= pivot:         # 피봇보다 크거나 같은 값이면, j를 감소(이동)
            j -= 1
        if i < j:                               # i, j가 중지된 지점에서 i, j 지점의 값을 교환
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]             # i > j인 지점에서 피봇값과 교환

    return j                            # 피봇의 위치 반환환

def QuickSort(l, r):

    if l < r:
        s = partition(l, r)
        QuickSort(l, s-1)
        QuickSort(s+1, r)

A = [7, 2, 5, 3, 4, 5]
N = len(A)
QuickSort(0, N-1)
print(A)


# Lomuto 파티션 방법이 있음 → 효율성 문제로 그냥 넘어가도 된다
