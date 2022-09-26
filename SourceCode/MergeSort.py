'''
병합 정렬 : 외부 정렬의 기본이 되는 정렬 알고리즘, 멀티코어 CPU나 다수의 프로세서에서
정렬 알고리즘 병렬화를 위해 병합 정렬 알고리즘 활용

퀵 정렬 : 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘
생물 정보 공학에서 특정 유전자를 효율적으로 찾는데 접미어 배열과 함께 사용

최근접 점의 쌍문제에 분할 정복을 사용할 수 있다
: 2차원 평면상의 n개의 점이 입력으로 주어질 때, 거리가 가장 가까운 한 쌍의 점을 찾는 문제
컴퓨터 그래픽스, 컴퓨터 비전, 지리 정보 시스템, 항공 트래픽 제어, 마케팅(신규 가맹정 위치 선정) 등의 분야
'''

# 리스트를 사용할 경우 자료의 비교 연산과 이동 연산이 발생해서 비효율적
# 연결 리스트를 사용할 경우 비효율적 단점을 극복해서 효과적 구현 가능

''' # 리스트를 사용한 경우
def merge_sort(lst):
    print(lst)
    # 쪼갤 수 없는 단계에서 중단
    if len(lst) <= 1:
        return lst

    # 왼쪽과 오른쪽을 쪼개서 사용
    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
    # l, r은 정렬된 리스트
    ret = []

    while l and r:      # 왼쪽, 오른쪽 리스트가 빌 때 까지 진행
        if l[0] <= r[0]:
            ret.append(l.pop(0))        # 왼쪽이 더 작을 때 왼쪽 리스트 값을 가져와서 append
        elif l[0] > r[0]:
            ret.append(r.pop(0))        # 오른쪽이 더 작을 때 오른쪽 리스트 값을 가져와서 append

    # while문이 동작하면서 l 혹은 r의 한쪽이 비었을 경우, 나머지 값 입력
    if l: ret.extend(l)
    if r: ret.extend(r)

    return ret          # 병합한 리스트를 제출


arr = [69, 30, 10, 2, 16, 8, 32, 21]
print(merge_sort(arr))


'''
# 인터넷 블로그 코드 - 인덱스 사용: 리스트 사용의 낭비를 줄일 수 있다.
def merge_sort(lst):
    # 리스트 분할 - 최소단위까지 분할
    if len(lst) < 2:            # 리스트의 크기가 2보다 작을 때 = 더이상 나누어질 수 없을 때
        return lst              # 리스트를 반환

    # 리스트 분할 - mid를 기준으로 좌, 우를 구분
    mid = len(lst) // 2                 # 중간인덱스 mid
    left = merge_sort(lst[:mid])        # mid 이전 리스트 : left
    right = merge_sort(lst[mid:])       # mid 이후 리스트 : right

    # 리스트 병합
    merge_arr = []              # 병합된 리스트를 담을 새로운 리스트 생성
    l = r = 0                   # 왼쪽, 오른쪽 기준 인덱스
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1

    # left or right 중 남아있는 값을 병합정렬에 넣어줌
    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr



# 연결 리스트를 사용하는 경우는?
