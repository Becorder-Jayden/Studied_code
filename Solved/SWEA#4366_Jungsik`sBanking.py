import sys
sys.stdin = open('../Solving/input.txt')

def exp(object, jinsu):
    possible = []
    obj = list(object)
    N = len(object)
    for i in range(N):
        for j in range(jinsu):
            temp = obj[i]             # obj[i]의 원본을 따로 잠시 저장
            obj[i] = str(j)

            ret = ''
            for k in obj[:]:          # 가능한 진수 값을 생성
                ret += k
            possible.append(ret)      # possible 리스트에 저장

            obj[i] = temp             # obj[i]를 원래 상태로 복구

    return set(possible)              # 중복된 값을 제거하기 위해 set 사용

T = int(input())
for tc in range(1, T+1):
    binary = input()
    triad = input()
    possible = []

    bin, tri = [], []

    for i in exp(binary, 2):
        bin.append(int(i, 2))

    for i in exp(triad, 3):
        tri.append(int(i, 3))

    for i in bin:
        if i in tri:
            print(f'#{tc} {i}')