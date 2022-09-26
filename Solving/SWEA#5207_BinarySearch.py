import sys
sys.stdin = open('input.txt')

# 9/27 블로거 코드 인용
# 이진탐색을 진행하기 위해 리스트는 오름차순이 되어있어야 한다
# 지표의 사용, break, continue 조금더 활용하기
# 이진탐색 반복문형, 재귀형 모두 활용할 수 있어야 한다

def BinarySearch(arr, i):
    global cnt

    left = 0
    right = len(arr) - 1

    flag = -1                       # flag 지표 사용, 오왼오왼은 허용하되, 오오왼왼, 왼왼오오 등을 걸러내기 위함
    while left <= right:
        mid = (left+right)//2

        if arr[mid] == i:
            cnt += 1
            return

        elif arr[mid] > i:
            if flag == 0:           # 이미 지표가 왼쪽 탐색을 했음을 나타냄 → 그대로 종료
                break
            right = mid - 1
            flag = 0
        else:
            if flag == 1:           # 이미 지표가 오른쪽 탐색을 했음을 나타냄 → 그대로 종료
                break
            left = mid + 1
            flag = 1


answer_li = []
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()                                ## 이진탐색의 대상이 되는 리스트는 오름차순 정렬되어 있어야 한다. 
    cnt = 0
    for i in B:
        BinarySearch(A, i)

    answer_li.append(f'#{tc} {cnt}')
print('\n'.join(answer_li))