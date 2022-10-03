import sys
sys.stdin = open('input.txt')

def Subset(arr):
    global answer
    ret = []
    for i in range(1<<len(arr)):
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        if subset == []:
            continue
        elif sum(subset) == S:
            answer += 1


N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
Subset(arr)
print(answer)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
Subset(arr)
print(answer)
