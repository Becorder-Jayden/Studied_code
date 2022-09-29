import sys
sys.stdin = open('../Solving/input.txt')

# 메모리 초과 오답 발생 → 해결
# 암호의 끝자리가 1로 끝난다는 점을 이용해서 적은 메모리로 암호를 추출할 수 있어야 함
# 딕셔너리를 사용해서 쉽게 암호를 10진수로 변경할 수 있다

'''
[1] 숫자 dict 저장
[2] for i range(1, 32, 4):
        ans.append(''.join(map (str, li[i:i+3])))
[3] odd = ans[0] + ans[2] + [4] + [6]
    even = ans[1] + [1] + [3] + [5]
    if (add*3 + even + ans[7]) % 10 == 0:
        return add+even
    else:
        return 0
'''

# dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
#         '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
#
# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     arr = [input() for i in range(N)]
#     li = []             # 해석된 암호가 저장될 공간
#     password = 0        # 암호가 입력된 지점을 확인하기 위한 변수
#     last = 0            # 암호의 마지막 지점 인덱스를 확인하기 위한 변수
#
#     # 암호가 입력된 공간을 확인, 암호 마지막 인덱스를 이용해서 메모리 소모를 줄임
#     for i in arr:
#         for j in range(M-1, -1, -1):
#             if i[j] == '1':
#                 last = j
#                 break
#         password = i
#         if last:
#             break
#
#     binary = password[last-55:last+1]       # 마지막 인덱스로부터 56번째 값까지가 주어진 암호
#     for i in range(0, 56, 7):
#         li.append(dict[binary[i:i+7]])
#
#     odd = even = 0
#     for i in range(8):          # 8: 암호의 묶음
#         if i % 2 == 0:
#             odd += li[i]
#         else:
#             even += li[i]
#
#     if (odd*3+even)%10 == 0:
#         answer = odd + even
#     else:
#         answer = 0
#     print(f'#{t+1}', answer)


''' 실패한 코드 : 메모리 초과
     li = []
     cnt = 0
     for i in arr:
         if '1' in i:
             cnt += 1
     for i in arr:
         for j in range(0, len(i), 7):
             if i[j:j+7] in dict:
                 if len(li) <= cnt:
                     li.append(dict[i[j:j+7]])
'''


# =============== 교수님 추가 설명 ===============
'''
가변길이를 사용하기 전에 갯수를 체크해보려고 함 
딕셔너리에 해독 코드가 아니라 비율을 이용하는 방법, 딕셔너리의 key값은 immutable일 때만 가능
→ immutable 타입인 튜플을 사용
'''
P = {(2,1,1): 0, (2,2,1): 1, (1,2,2): 2, (4,1,1): 3, (1,3,2): 4,
     (2,3,1): 5, (1,1,4): 6, (3,1,2): 7, (2,1,3): 8, (1,1,2): 9}


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    line_set = set()                # 셋 저장공간을 만들어서 활용 : 탐색 시간이 O(N)
    
    for _ in range(N):
        t = input().rstrip('0')
        if t:
            line_set.add(t)
            
            
    code_set = set()
    for line in line_set:
        # line을 2진수 문자열로 변환
        i = len(line) - 1       # 마지막 인덱스를 나타내는 i
        while i >= 0:          # i는 적어도 56 이상
            if line[i] == '1':
                codes = []
                # 0101 패턴을 8번 반복
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0
                    while line[i] == '0': i -= 1    # plus: 구현의 테크닉
                    while line[i] == '1': c4 += 1; i -= 1   # 1의 개수 카운팅
                    while line[i] == '0': c3 += 1; i -= 1   # 0의 개수 카운팅
                    while line[i] == '1': c2 += 1; i -= 1   # 1의 개수 카운팅
                    # c1 = 7 - (c2 + c3 + c4)
                    # i -= c1
                    # codes.append(P[(c1, c2, c3, c4)])
                    ratio = min(c2, c3, c4)
                    codes.append(P[(c2//ratio, c3//ratio, c4//ratio)])
                code_set.add(tuple(codes))
            i -= 1

    ans = 0
    odd = even = 0

    for codes in code_set:
        odd = codes[1] + codes[3] + codes[5] + codes[7]
        even = codes[0] + codes[2] + codes[4] + codes[6]
        if (odd*3+even) % 10 == 0:
            ans += odd + even
    print(ans)


'''
가변 코드
카운팅한 값 중에 가장 작은 값
x1          x2          x3
=============================
3:2:1:1 

카운팅한 값(비율)에서 가장 작은 수로 나누면 비율을 구할 수 있다. 
가변길이 → 제일 작은 값으로 나누는 아이디어 
하나의 값(비율)은 나머지 세개의 비율을 알면 구할 수 있다. 암호 길이가 8인 것을 알기 때문
'''