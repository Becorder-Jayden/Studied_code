import sys
sys.stdin = open('../Solving/input.txt')

# 9/20 못품..

# '0000000'으로 split()?
# 16진수로 표현된 암호문에 0이 포함된 경우가 있음

dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
       '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
       'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
bin_dic = {
    '0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'
}

T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    leng = []
    for i in arr:
        leng.append(len(i.strip('0')))
    l = leng.index(max(leng))

    for i in range(len(arr)):
        if i == l:
            password = arr[i].strip('0')

    binary = ''
    for i in password:
        binary += dic[i]

    for i in binary.split('0000000'):
        if i:
            li = []
            password = i.rstrip('0')
            for i in range(len(password), -1, -7):
                if password[i-7:i] in bin_dic:
                    li.append(bin_dic[password[i-7:i]])

            print(li)

            a = ''
            for i in list(reversed(li)):
                a += i

            odd = even = 0
            for i in range(len(a)):
                if i%2 == 0:
                    odd += int(a[i])
                else:
                    even += int(a[i])
            if (odd*3+even)%10 == 0:
                print(f'#{t+1}', odd+even)
            else:
                print('No', odd*3+even, a)


# =============== 교수님 추가 설명 ===============
'''
가변길이를 사용하기 전에 갯수를 체크해보려고 함 
딕셔너리에 해독 코드가 아니라 비율을 이용하는 방법, 딕셔너리의 key값은 immutable일 때만 가능
→ immutable 타입인 튜플을 사용
'''
P = {(3,2,1,1): 0, (2,2,2,1): 1, (2,1,2,2): 2, (1,4,1,1): 3, (1,1,3,2): 4,
     (1,2,3,1): 5, (1,1,1,4): 6, (1,3,1,2): 7, (1,2,1,3): 8, (3,1,1,2): 9}


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    line_set = set()                # 셋 저장공간을 만들어서 활용 : 탐색 시간이 O(N)
    for _ in range(N):
        t = input().rstrip('0')
        if t:
            line_set.add(t)

    for line in line_set:
        i = len(line) - 1       # 마지막 인덱스를 나타내는 i
        while i >= 0:          # i는 적어도 56 이상
            if line[i] == '1':
                codes = []
                # 0101 패턴을 8번 반복
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0
                    while line[i] == '1': c4 += 1; i -= 1   # 1의 개수 카운팅
                    while line[i] == '0': c3 += 1; i -= 1   # 0의 개수 카운팅
                    while line[i] == '1': c2 += 1; i -= 1   # 1의 개수 카운팅
                    c1 = 7 - (c2 + c3 + c4)
                    i -= c1
                    print(c1, c2, c3, c4, P[(c1, c2, c3, c4)])
            i -= 1
    ans = 0
    odd = codes[1] + codes[3] + codes[5] + codes[7]
    even = codes[0] + codes[2] + codes[4] + codes[6]
    if (odd*3+even)%10 == 0:
        ans += odd + even
    print(ans)