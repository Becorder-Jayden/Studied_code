import sys
sys.stdin = open('../Solving/input.txt')

# 16진수 → 2진수 → 10진수 순서대로 변환
dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

T = int(input())
for t in range(T):
    inp = input()

    # 16진수를 2진수로 변환, dictionary 이용
    binary = ''
    for i in inp:
        binary += dict[i]

    # 7bit 마다 입력된 2진수를 10진수로 변환
    answer = []
    n = 0
    for i in range(len(binary)):
        n = int(binary[i]) + n*2                    # 앞에서부터 탐색 → 업데이트 = 기존의 값*2 + 새로운 값(0 or 1)
        if (i % 7) == 6 or i == len(binary)-1:      # % 연산으로 7번째 마다 or (조건 2 마다)
            answer.append(n)
            n = 0

    print(f'#{t+1}', *answer)
