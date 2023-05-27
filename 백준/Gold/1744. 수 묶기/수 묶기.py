from queue import PriorityQueue

N = int(input())
p_pq = PriorityQueue()      # 매번 정렬을 할 수 있도록 우선순위 큐 사용
m_pq = PriorityQueue()      # 매번 정렬을 할 수 있도록 우선순위 큐 사용
o_cnt = 0
z_cnt = 0
total = 0

for i in range(N):
    val = int(input())
    if val > 1:
        p_pq.put(val * -1)
    elif val < 0:
        m_pq.put(val)
    elif val == 0:
        z_cnt += 1
    elif val == 1:
        o_cnt += 1

while p_pq.qsize() > 1:
    a = p_pq.get() * -1
    b = p_pq.get() * -1
    total += a * b

if p_pq.qsize() > 0:
    total += p_pq.get() * -1

while m_pq.qsize() > 1:
    a = m_pq.get()
    b = m_pq.get()
    total += a * b

if m_pq.qsize() > 0:
    if z_cnt == 0:
        total += m_pq.get()
        
if o_cnt:
    total += o_cnt * 1

print(total)