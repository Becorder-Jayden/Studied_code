import sys
sys.stdin = open('../Solving/input.txt')

T = int(input())
for t in range(T):
    lst = list(map(int, input()))
    ans = []                        # 정답을 담을 리스트 생성
    n = 0
    for i in range(len(lst)):
        n = lst[i] + n*2            # 이진수를 십진수의 값으로 변환

        if (i % 7) == 6:              # 매 7개 인덱스마다
            ans.append(n)             # ans 리스트에 저장
            n = 0                     # n의 값 초기화

    print(f'#{t+1}', *ans)
