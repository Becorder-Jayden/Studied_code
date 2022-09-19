import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    inp = input().split()
    N, hex = int(inp[0]), inp[1]

    print(f'#{t+1}', end=' ')       # 예제 번호
    for i in hex:                   # 16진수의 값을 10진수로 변환 후, 4자리 2진수로 변환
        print(format(int(i, 16), '04b'), end='')
        # int(i, 16): int를 이용한 16진수 변환, format(i, '04b'): format을 이용한 2진수(b) 변환
        # 진수변환에 bin, hex등의 메서드를 사용할 수도 있다.
    print()
