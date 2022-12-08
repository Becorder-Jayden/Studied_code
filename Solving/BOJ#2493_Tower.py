import sys
sys.stdin = open('BOJ#2493_Tower.txt')

# 거꾸로 만들어와야?: x -> stack 문제

N = int(input())    # 500,000 이하 -> 완전탐색으로 구현하면 시간초과 발생 우려
towers = list(map(int, input().split()))
lst = [(0, 0)]  # 초기 값으로 (0, 0)을 보유
ans_lst = []    # 정답 리스트

for i in range(len(towers)):
    # stack에 쌓여있는 마지막 높이보다 현재의 탑이 더 높을 경우
    if lst[-1][0] < towers[i]:      # cf. 탑은 서로 높이가 다르므로 높이가 동일한 경우에 대해 생각 x
        # stack의 마지막 값 삭제 : 반복 -> 현재 탑보다 큰 높이가 나올 때까지
        while lst[-1][0] < towers[i]:
            lst.pop()
            # 만약 lst가 빈칸이 되었을 경우 정답 리스트에 0을 추가하고 종료, 0: 왼쪽 방향에 현재 탑보다 높은 탑이 없음
            if len(lst) == 0:
                ans_lst.append(0)
                break
        # lst에 값이 남아있을 때: 현재 탑보다 높은 탑 존재 -> 남아있는 탑의 인덱스 입력
        if lst:
            ans_lst.append(lst[-1][1])
        lst.append((towers[i], i+1))    # 현재의 탑 높이 기록
    else:   # 마지막에 기록한 탑의 높이가 현재 탑보다 높을 때
        lst.append((towers[i], i+1))    # 현재 탑의 정보(높이, 위치) 기록
        ans_lst.append(i)   # 정답 리스트에 현재 탑 위치 기록
print(*ans_lst)
