import sys
sys.stdin = open('BOJ#14888_InsertOperator.txt')

# Q. 비효율 제거 하고 싶은데 방법은 어떻게?
# ex) [+, +, -, *, /]일 때, +를 중복해서 계산하는 부분이 발생?

# 순열 vs 조합 : 만들 수 있는 모든 경우의 수 생성
# 순열: 순서가 다를 경우 다른 경우       ex) (1,2,3), (2,1,3), (3,2,1) ...
# 조합: 순서가 다르더라도 같은 경우       ex) (1,2,3), (1,2,4), (1,3,4) ... => (3,2,1)x (2,4,1)x ..

def perm(level, temp):      #  순열 사용
    global visited, new_cal
    if level == len(cal_lst):
        for i in range(len(A)-1):
            new_cal.append(A[i])
            new_cal += temp[i]
        new_cal.append(A[len(A)-1])
        # print('new_cal:', new_cal)


        stack = [new_cal[0]]
        # print(stack)
        for i in range(len(new_cal)):
            if new_cal[i] in ['+', '-', '*', '/']:
                a = stack.pop()
                b = new_cal[i+1]
                if new_cal[i] == '+':
                    stack.append(a+b)
                elif new_cal[i] == '-':
                    stack.append(a-b)
                elif new_cal[i] == '*':
                    stack.append(a*b)
                elif new_cal[i] == '/':
                    if a >= 0:
                        stack.append(a//b)
                    else:
                        stack.append(-(abs(a)//b))
        total_cal_lst.append(stack[0])
        # print('new_cal:', new_cal, stack[0])
        new_cal = []
        return

    for i in range(len(cal_lst)):
        if visited & (1<<i): continue
        visited += 1 << i
        perm(level+1, temp+[cal_lst[i]])
        visited -= 1 << i


N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))     # 연산자 개수: +, -, *, /
cal_lst = []
new_cal = []
visited = 0
total_cal_lst = []


# cal_lst 생성
for i in range(len(C)):
    if i == 0:
        for j in range(C[0]):
            cal_lst += ['+']
    elif i == 1:
        for j in range(C[1]):
            cal_lst += ['-']
    elif i == 2:
        for j in range(C[2]):
            cal_lst += ['*']
    elif i == 3:
        for j in range(C[3]):
            cal_lst += ['/']

# cal_lst를 가지고 만들 수 있는 모든 경우의 수 구하기
# comb(0, -1, [])
perm(0, [])
print(max(total_cal_lst))
print(min(total_cal_lst))