import sys
sys.stdin = open('BOJ#14501_Resignation.txt')

N = int(input())
for n in range(N):
    T, P = map(int, input().split())
    print(T, P)