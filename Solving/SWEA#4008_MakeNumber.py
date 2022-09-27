import sys
sys.stdin = open('input.txt')

## 아직 못품 !!!


# 연산자의 조합 만들기
def permutation(i, k):
    if i == k:          # 인덱스 i == 원소의 개수
        li = cal_list[:]
        set_list.append(tuple(li))
    else:
        for j in range(i, k):
            cal_list[i], cal_list[j] = cal_list[j], cal_list[i]     # 자리를 바꿈
            permutation(i+1, k)
            cal_list[i], cal_list[j] = cal_list[j], cal_list[i]



for tc in range(1, int(input())+1):
    N = int(input())
    has = list(map(int, input().split()))       # [+, -, *, /]
    numbers = list(map(int, input().split()))
    cal_list = []
    for i in range(len(has)):
        if i == 0:
            for i in range(has[i]):
                cal_list.append('+')
        elif i == 1:
            for i in range(has[i]):
                cal_list.append('-')
        elif i == 2:
            for i in range(has[i]):
                cal_list.append('*')
        elif i == 3:
            for i in range(has[i]):
                cal_list.append('/')

    print(cal_list)

    # # 조합을 만들기 위한 변수 생성
    # set_list = []
    # permutation(0, len(cal_list))
    #
    # answer_li = []
    # # 계산 식 생성
    # for i in list(set_list):
    #     S = [numbers[0]]
    #     for j in range(len(i)):
    #         if i[j] == '+':
    #             a = S.pop()
    #             b = numbers[j+1]
    #             S.append(a+b)
    #         elif i[j] == '-':
    #             a = S.pop()
    #             b = numbers[j+1]
    #             S.append(a-b)
    #         elif i[j] == '*':
    #             a = S.pop()
    #             b = numbers[j+1]
    #             S.append(a*b)
    #         elif i[j] == '/':
    #             a = S.pop()
    #             b = numbers[j+1]
    #             S.append(int(a/b))
    #     answer_li.append(S[0])
    #
    # print(answer_li)