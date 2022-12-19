import sys
sys.stdin = open('BOJ#1918_BackwardNotation.txt')

# 블로그 풀이 해석
# 어려웠던 점: 괄호에 대한 처리를 어떻게 해야 할지
# 괄호에 대한 처리
#   여는 괄호일 때, 스택에 담고 넘어간다.
#   덧셈, 뺄셈일 때 여는 괄호가 나올 때까지 연산자를 꺼내서 결과값에 입력해준다
#   닫는 괄호일 때, 여는 괄호가 나올 때까지 연산자를 꺼내서 결과값에 입력하고, 여는 괄호를 제거한다
# isalpha 메서드를 이용하면 영문자를 골라내기가 수월해진다

# tip : 이전 연산자들의 처리에 대해서 => 다음 연산자를 확인할 때 처리해도 괜찮다
# stack 구조


inp = list(input())
stack = []      # 스택 저장 공간
res = ""

# inp 값의 요소 확인
for i in inp:
    if i.isalpha():     # i.isalpha(): 만약 i가 영문자라면 True
        res += i        # res에 문자 입력

    elif i == '(':          # 여는 괄호: stack에 담는다
        stack.append(i)

    elif i == '*' or i == '/':      # 곱셈 또는 나눗셈
        # stack의 꼭대기 연산자가 같은 우선순위의 연산자일 경우
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()  # res에 모든 연산자를 입력하고
        stack.append(i)         # stack에 현재 연산자 입력

    elif i == '+' or i == '-':      # 덧셈 또는 뺄셈
        # stack의 꼭대기 연산자가 여는괄호가 아닌 동안
        while stack and stack[-1] != '(':
            res += stack.pop()  # res에 모든 연산자를 입력
        stack.append(i)         # stack에 현재 연산자 입력

    elif i == ')':          # 닫는 괄호일 때
        while stack and stack[-1] != '(':   # 여는 괄호가 나올 때 까지
            res += stack.pop()      # 연산자를 빼서 res에 입력
        stack.pop()     # 여는 괄호까지 제거

while stack:        # stack에 남은 값들에 대해서
    res += stack.pop()      # stack의 위에 쌓인 연산자부터 res에 입력

print(res)