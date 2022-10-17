import sys
sys.stdin = open('BOJ#14503_RobotCleaner.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(N, M)
for i in arr:
    print(i)