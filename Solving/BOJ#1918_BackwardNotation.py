import sys
sys.stdin = open('BOJ#1918_BackwardNotation.txt')

'''
A+B*C-D/E   => ABC*+DE/-
A*(B+C)     => ABC+*
A+B         => AB+
A+B*C       => ABC*+
A*B+C       => AB*C+
A+B*C-D/E   => ABC*+DE/-
'''

# 중위 → 후위
# 1. 연산자 우선순위에 따라 괄호로 묶는다.
# 2. 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨준다.


# 곱셈(나눗셈일 경우) 괄호 추가
for tc in range(4):
    inp = list(input())
    stack = []
    for i in inp:
        stack.append(i)
        if len(stack) > 2 and (stack[-2] == '*' or stack[-2] == '/'):
            tempB = stack.pop()
            cal = stack.pop()
            tempA = stack.pop()

            stack.append('(')
            stack.append(tempA)
            stack.append(cal)
            stack.append(tempB)
            stack.append(')')

    print(''.join(stack))