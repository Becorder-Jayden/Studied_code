import sys
sys.stdin = open('BOJ#10817_3Numbers.txt')

inp = list(map(int, input().split()))
print(sorted(inp)[1])