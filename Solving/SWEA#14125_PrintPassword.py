import sys
sys.stdin = open('input.txt')

'''
[1] 16진수 → 2진수(str)로 저장
[2] 우측 끝부터 '1' 찾기       # 끝을 가리키는 인덱스 값을 저장할 변수 사용하기 ex) e
    e = len(lst) - 1
    while lst[e] == '0':
        e -= 1
[3] 최초 시작 위치부터 6개씩 dict 변환해서 ans([])에 저장
    for i in range((e-5)%6, e, 6):
        ans.append(dict[i:i+6])
'''


dict = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100',
        '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',
        'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110',
        'F':'1111'}

pw_dict = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
        '110111': 5, '001011': 6, '111101': 7, '011001': 8, '011111': 9}

T = int(input())
for t in range(T):
    inp = input()

    # 1. 2진수로 저장
    binary = ''
    for i in inp:
        binary += dict[i]

    # 2. 우측 끝 '1' 찾기
    last = 0
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            last = i
            break

    # 3. 10진수로 변환
    answer = []


    # 3-1 내가 임의로 적용해본 방식
    # pwd = binary[last-6*(last//6)+1:last+1]
    #
    # for i in range(0, len(pwd), 6):
    #     part = pwd[i:i+6]
    #     answer.append(pw_dict[part])

    # 3-2 교수님이 알려주신 방식
    for i in range((last-5)%6, last, 6):            # last 인덱스, % 연산 활용
        answer.append(pw_dict[binary[i:i+6]])       # 불필요한 메모리 낭비 최소화 ***


    print(f'#{t+1}', *answer)




''' 교수님 예제 코드
T = int(input())
for t in range(T):
    inp = input()
    li = []
    for i in inp:
        li += dict[i]

    # [2] 우측 끝 '1' 찾기
    e = len(li)-1
    while li[0] == 0:
        e -= 1

    # [3] 시작 위치부터 6개씩, 암호를 숫자로 변환
    for i in range((e-5)%6, e, 6):
        ans.append(dict[i:i+6])
    ans = []

    print(f'#{t+1}', *ans)
'''
