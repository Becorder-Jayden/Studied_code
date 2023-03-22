from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))
myDeque = deque()

# ([인덱스][값]) 형태로 myDeque에 데이터 관리
for i in range(N):
    
    # 새로운 값이 기존의 값보다 클 때까지 기존의 값 (끝에서부터) 제거
    while myDeque and myDeque[-1][0] > arr[i]:
        myDeque.pop()
    myDeque.append((arr[i], i))     # 새로운 값 입력

    # 슬라이딩 윈도우가 인덱스 범위에서 벗어난 경우 제거
    if myDeque[0][1] <= i-L:
        myDeque.popleft()

    print(myDeque[0][0], end=' ')
        