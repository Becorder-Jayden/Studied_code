from queue import PriorityQueue

N = int(input())
primary_queue = PriorityQueue()         # 우선순위 큐 정의
answer = 0

# 입력값을 primary_queue에 삽입
for _ in range(N):
    primary_queue.put(int(input()))

# primary_queue가 1보다 클 때: 2개씩 뽑기 때문
while primary_queue.qsize() > 1:
    
    # 가장 작은 값 2개를 뽑아 더한 값을 answer에 저장
    got1 = primary_queue.get()
    got2 = primary_queue.get()
    temp = got1 + got2
    answer += temp
    
    # temp 값을 우선순위 큐에 넣고 정렬
    primary_queue.put(temp)

print(answer)