checkList = [0] * 4
myList = [0] * 4
checkSecret = 0     # 최소량을 만족하는 비밀번호의 갯수

def myAdd(c):       # 새로 들어온 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myRemove(c):        # 제거된 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
String = list(input())
answer = 0
checkList = list(map(int, input().split()))

# 초기 조건에 만족하는 요소 확인
for i in range(4):
    if checkList[i] == 0:       # checkList 요소가 0: 최소 조건을 만족
        checkSecret += 1

# 첫번째 슬라이딩 윈도우 확인
for i in range(P):
    myAdd(String[i])
if checkSecret == 4:
    answer += 1

# 슬라이딩 윈도우 이동하면서 값 확인
for right in range(P, S):
    left = right - P       # 왼쪽 포인터 = 오른쪽 포인터 - 슬라이딩 윈도우의 크기
    myAdd(String[right])        # 오른쪽 이동: 추가
    myRemove(String[left])      # 왼쪽 이동: 삭제
    if checkSecret == 4:
        answer += 1

print(answer)
