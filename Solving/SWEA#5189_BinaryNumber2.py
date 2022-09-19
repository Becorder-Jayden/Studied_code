import sys
sys.stdin = open('input.txt')

'''
소수의 이진수 변환
소수부분에 2를 곱했을 때, 정수부분을 값으로 한다
ex) 0.625
→ 0.625 * 2 = 1.250 → 1
→ 0.250 * 2 = 0.500 → 0
→ 0.500 * 2 = 1.000 → 1

따라서 0.625의 이진수는 0.101(2)가 된다
'''

def binary(float):
    answer = ''
    while True:
        if len(answer) == 13 or int(float) or float == 0:
            break
        float = float * 2
        if float >= 1:
            answer += '1'
            float -= 1
        else:
            answer += '0'

    return answer


T = int(input())
for t in range(T):
    inp = float(input())
    print(f'#{t+1}', end=' ')
    if len(binary(inp)) == 13:
        print('overflow')
    else:
        for i in binary(inp):
            print(i, end='')
        print()
