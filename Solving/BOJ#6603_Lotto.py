import sys
sys.stdin = open('input.txt')

while True:
    inp = list(input().split())
    if inp[0] == '0':
        break
    S = list(inp[1:])
    print(S)