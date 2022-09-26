# 선형 큐
# 원형 큐


'''
* 공백상태: front == rear
* 포화상태: (rear+1)%n = front
'''


# 공백상태 확인: front == rear일 때
def isEmpty():
    return front == rear

# 포화상태 확인
def isFull():
    return (rear+1)%len(Q) == front

# 원소의 삽입
def deQueue(item):
    global rear

    if isFull():
        return
    else:
        rear = (rear+1)%len(Q)
        Q[rear] = item

# 원소의 삽입
def delete():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front+1)%len(Q)