import sys
sys.stdin = open('SWEA#4012_Cook.txt')

# Q. N이 6개 이상일 때는 어떻게 해야 하는건지 모르겠음..
# A. 부분 조합을 만드는 함수를 추가해서 사용

# N개의 숫자 중 N//2개 선택
# 스터디 → 2개의 파트로 나눈 것을 이용해 다시 2개씩 조합 생성해볼 것

# with 종호 == 현자타임, 종호는 luv 입니다.

def comb_part(lst):
    S = 0
    for i in lst:
        for j in lst:
            if i != j:
                S += mix[i][j]
    return S


def comb(level, start, temp):
    if level == N//2:
        set_A, set_B = set(temp), set(arr)-set(temp)
        li_A.append(set_A)
        li_B.append(set_B)
        return
    for i in range(start+1, N):
        comb(level+1, i, temp+[arr[i]])


for tc in range(1, int(input())+1):
    N = int(input())
    mix = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    li_A = []
    li_B = []
    ans = 0xfffff
    comb(0, -1, [])

    if len(li_A)%2 == 1:
        for i in range(len(li_A)//2+1):
            ans = min(ans, abs(comb_part(li_A[i])-comb_part(li_B[i])))
    else:
        for i in range(len(li_A)//2):
            ans = min(ans, abs(comb_part(li_A[i])-comb_part(li_B[i])))

    print(f'#{tc} {ans}')
