# 반드시 정렬된 상태에서 이진 탐색을 진행해야 함
def binary_search(arr, low, high, key):
    # 중간 위치를 선택
    mid = (low+high)//2         # 기준을 삼을 중간 인덱스
    
    # 범위를 조절하면서 탐색 진행
    while low <= high:          # low <= high 조건을 만족할 때까지 진행
        if arr[mid] == key:         # 기준 값이 찾는 값일 때, 반환
            return mid
        elif arr[mid] > key:        # 기준 값이 찾는 값보다 클 때
            high = mid - 1              # 범위를 기준 값-1 범위에서 탐색
        else:                       # 기준 값이 찾는 값보다 작을 때
            low = mid + 1               # 범위를 기준 값+1 범위에서 탐색
    
    return - 1          # 찾을 수 없을 때

# 다른 버전(재귀 이용)
def binary_search_recur(arr, low, high, key):
    # 찾을 수 없는 경우
    if low >= high:
        return -1

    mid = (low+high) >> 1       # == (low+high)//2

    # 기준 값이 찾는 값일 때
    if arr[mid] == key:
        return mid

    # 기준 값보다 찾는 값이 작을 때
    elif arr[mid] > key:
        return binary_search_recur(arr, low, mid-1, key)    # low ~ mid-1 범위 탐색

    # 기준 값보다 찾는 값이 클 때
    else:
        return binary_search_recur(arr, mid+1, high, key)   # mid+1 ~ high 범위 탐색
