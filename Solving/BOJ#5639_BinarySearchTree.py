import sys
sys.stdin = open('input.txt')

# 이진 탐색 트리의 push, pull은 어떻게 구현할 수 있을까?


# 입력값 받기
try:
    li = []
    while True:
        inp = int(input())
        li.append(inp)
except: pass

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item

    p = hsize // 2
    c = hsize

    while p and H[p] < H[c]:
        H[p], H[c] = H[c], H[p]
        p = c//2
        c = p

N = len(li)
H = [0] * (N+1)

hsize = 0


for i in li:
    push(i)

print(H)
