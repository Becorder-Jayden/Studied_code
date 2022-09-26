import sys
sys.stdin = open('input.txt')

# 파이썬의 sort()는 퀵정렬 + 'OOOOO' 을 이용해서 구현되고 있다.
# 원래대로라면 SourceCode 파일에 있는 quick 정렬 구현함수를 확인할 것

answer_li = []
for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer_li.append(f'#{tc} {arr[N//2]}')

print('\n'.join(answer_li))