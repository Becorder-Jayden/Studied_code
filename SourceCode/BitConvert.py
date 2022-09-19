arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

# int 메서드를 이용한 간단한 출력 방법
for i in range(0, len(arr), 7):
    b = arr[i:i+7]
    print(int(b, 2))


# 예시) 1234로 바꾸고 싶을 때
inp = [1,2,3,4]
num = 0
for i in inp:
    num = num * 10 + i
# print(num)


# for 문을 사용해 2진수의 10진수 값 출력
for i in range(0, len(arr), 7):
    num = 0
    for j in range(i, i+7):
        num = num * 2
        if arr[j] == '1':
            num += 1
    # print(num, end=' ')


# 비트 연산자 사용
for i in range(0, len(arr), 7):
    num = 0
    for j in range(7):
        if arr[i+j] == '1':
            num = num | (1 << (6 - j))
    # print(num, end=' ')

