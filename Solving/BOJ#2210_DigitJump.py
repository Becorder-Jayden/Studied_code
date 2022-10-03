import sys
sys.stdin = open('input.txt')

# 블로그 참고 수정
# 1: 입력값을 받아올 때 숫자가 아닌 '문자'로 받아옴
# 2: 만들어가는 과정을 변수에 담아 활용

'''
cf. 오류사항
li에 담을 값을 리스트 형태로 담아 진행하려고 했으나, 재귀가 return 되면서 li에 담은 값도 변하는 현상 발생
'''

dcol = [0, 0, -1, 1]
drow = [-1, 1, 0, 0]

def exp(col, row, number):
    if len(number) == 6:
        if number not in li:
            li.append(number)
        return

    for v in range(4):
        ncol = col + dcol[v]
        nrow = row + drow[v]
        if 0<=ncol<5 and 0<=nrow<5:
            exp(ncol, nrow, number + arr[ncol][nrow])               #2


arr = [list(map(str, input().split())) for _ in range(5)]           #1
li = []
for col in range(5):
    for row in range(5):
        exp(col, row, arr[col][row])

# print(li)
print(len(li))