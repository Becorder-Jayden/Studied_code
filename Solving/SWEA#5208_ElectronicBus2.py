import sys
sys.stdin = open('input.txt')

# 9/28 아직 못품

for tc in range(1, int(input())+1):
    charge = 0
    arr = list(map(int, input().split()))
    print(arr)
    print(tc)