import sys
sys.stdin = open('input.txt')

# 반례가 있나보다 오답처리 됨 → 완료 : visited 처리가 빠진 부분이 있었다
# 풀이 : cnt번째 경로들을 표기, 가장 큰 값을 갖는 값중 인덱스가 가장 큰 부분을 정답으로 출력

from collections import deque

def exp(s):
    queue = deque()
    for i in arr[s]:
        queue.append(i)
    cnt = 0
    while queue:
        cnt += 1
        for i in range(len(queue)):
            ns = queue.popleft()
            if visited[ns] == 0:        # 마지막 오류 수정
                visited[ns] = cnt
            for j in arr[ns]:
                if visited[j] == 0:
                    queue.append(j)
    return cnt

T = 10
for t in range(T):
    length, start = map(int, input().split())
    inp = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(0, len(inp), 2):
        frm, to = inp[i], inp[i+1]
        arr[frm].append(to)

    # 정답 값 출력
    answer = 0
    m = 0
    latest = exp(start)

    for i in range(101):
        if m <= visited[i]:
            m = visited[i]
            answer = i
    print(f'#{t+1}', answer)
