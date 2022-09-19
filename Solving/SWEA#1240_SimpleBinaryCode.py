import sys
sys.stdin = open('input.txt')

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

dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    li = []             # 해석된 암호가 저장될 공간
    password = 0        # 암호가 입력된 지점을 확인하기 위한 변수
    last = 0            # 암호의 마지막 지점 인덱스를 확인하기 위한 변수

    # 암호가 입력된 공간을 확인, 암호 마지막 인덱스를 이용해서 메모리 소모를 줄임
    for i in arr:
        for j in range(M-1, -1, -1):
            if i[j] == '1':
                last = j
                break
        password = i
        if last:
            break

    binary = password[last-55:last+1]       # 마지막 인덱스로부터 56번째 값까지가 주어진 암호
    for i in range(0, 56, 7):
        li.append(dict[binary[i:i+7]])

    odd = even = 0
    for i in range(8):          # 8: 암호의 묶음
        if i % 2 == 0:
            odd += li[i]
        else:
            even += li[i]

    if (odd*3+even)%10 == 0:
        answer = odd + even
    else:
        answer = 0
    print(f'#{t+1}', answer)


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
