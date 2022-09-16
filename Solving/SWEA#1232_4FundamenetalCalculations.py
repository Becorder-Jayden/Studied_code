import sys
sys.stdin = open("input.txt")

# 9/15 풀이 완료
# 후위 순회 방식 정의
def porder(v):
    global li
    if v == 0:
        return

    porder(L[v])        # 왼쪽 노드 탐색
    porder(R[v])        # 오른쪽 노드 탐색

    if P[v] not in ['+', '-', '*', '/']:        # 연산자가 아닐 때 스택에 담아 둠
        li.append(P[v])
    else:                                       # 연산자가 나왔을 때
        b = li.pop()                            # 스택에서 2개의 자료를 꺼냄
        a = li.pop()
        if P[v] == '+':                         # 계산이후 다시 스택에 삽입
            li.append(a+b)
        elif P[v] == '-':
            li.append(a-b)
        elif P[v] == '*':
            li.append(a*b)
        elif P[v] == '/':
            li.append(a//b)


T = 10
for t in range(T):
    N = int(input())

    # 이진트리 연결리스트 생성
    P = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)

    for n in range(N):
        inp = list(input().split())
        if len(inp) == 4:
            idx, cal, l, r = int(inp[0]), inp[1], int(inp[2]), int(inp[3])
            P[idx] = cal
            L[idx] = l
            R[idx] = r
        else:
            idx, val = int(inp[0]), int(inp[1])
            P[idx] = val
    li = []
    porder(1)                       # 1번 노드(루트 노드) 부터 실행
    print(f"#{t+1}", end=" ")       # 정답 형식 출력
    print(li[0])
