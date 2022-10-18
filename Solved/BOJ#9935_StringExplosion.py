import sys
sys.stdin = open("BOJ#9935_StringExplosion.txt")

str = input()
code = input()
stack = []

for i in str:
    stack.append(i)
    if stack[-len(code):] == list(code):
        del(stack[-len(code):])

if stack:
    print(''.join(stack))
else:
    print('FRULA')