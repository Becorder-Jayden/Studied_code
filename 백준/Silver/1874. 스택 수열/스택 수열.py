from collections import deque

N = int(input())
queue = deque([])
lst = []
ans_lst = []

for i in range(N):
    queue.append(int(input()))

for i in range(1, N+1):
    ans_lst.append('+')
    lst.append(i)
    while lst and lst[-1] == queue[0]:
        ans_lst.append('-')
        lst.pop()
        queue.popleft()
        
if lst == []:
    for i in ans_lst:
        print(i)
else:
    print("NO")
