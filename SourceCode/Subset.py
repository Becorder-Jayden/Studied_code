# 부분집합 구하기
'''
Power set = 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분집합
'''
## 설명이 필요: 완벽하게 이해하기 어렵다..


# 비트연산자 사용
arr = [1,2,3,4,5]
def Subset(arr):
    ret = []                # 생성된 부분집합을 반환할 리스트
    for i in range(1<<len(arr)):        # 부분집합의 개수 : 2**n
        subset = []                     # 부분집합을 담을 공간 마련
        for j in range(len(arr)):
            if i & (1<<j):              # '원소 i'와 '비트 연산자로 1을 이동시키는 값'을 & 연산 적용
                subset.append(arr[j])
        ret.append(subset)

    return ret

# print(Subset(arr))


# 부분집합의 상태 공간 트리 → 깊이 우선 탐색으로 모든 부분집합 생성 알고리즘
# 높이 k에 위치한 노드 = k개의 선택이 이루어진 상태

arr = [3, 6, 7]
n = len(arr)
bit = [0] * n

def SubsetRecursion(i, k):
    if i == k:                      # 모든선택이 끝난 상태, 상태공간트리의 단말 노드(leaf node)에 도달
        for j in range(k):
            if bit[j]:                  # 해당 노드의 비트를 이용해 표기
                print(arr[j], end=' ')
        print()
    else:                           # i != k 일 때, 단말 노드에 도달하지 못한 상태
        bit[i] = 0                      # bit[i]에 0을 넣고
        SubsetRecursion(i+1, k)             # i+1 깊이로 이동
        bit[i] = 1                      # bit[i]에 1을 넣고
        SubsetRecursion(i+1, k)             # i+1 깊이로 이동

SubsetRecursion(0, n)


'''
    i      binary       1<<j
----------------------------------
    0       0000        0000
    1       0001        0001
    2       0010        0010
    3       0011        0100
    4       0100        1000
    5       0101
    6       0110
    7       0111
    8       1000 
    9       1001
    10      1010
    ..       ..

1을 왼쪽 shift하게 되면, 

[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], ...
→ 0 까지 범위에서의 부분집합
→ 1 까지 범위에서의 부분집합
→ 2 까지 범위에서의 부분집합
→ 3 까지 범위에서의 부분집합
→ 4 까지 범위에서의 부분집합 의 형태로 진행되는 것을 볼 수 있다
'''