from collections import deque

# 탐색 방향 설정
dcol = [-1, 0, 1, 0]
drow = [0, -1, 0, 1]

def bfs(col, row):
    queue = deque()     # 데크 형식으로 저장공간 queue생성
    queue.append((col, row))    # 실행 위치의 값 추가
    visited[col][row] = 1       # 저장 위치 체크
    cnt = 0                 # 최단 경로의 거리

    # 큐가 빈 공간이 될 때까지
    while queue:
        cnt += 1    # 최단경로의 길이 + 1
        for i in range(len(queue)):         # 같은 레벨의 노드가 모두 진행될 수 있도록 len(queue) 사용
            col, row = queue.popleft()      # col, row를 뽑아냄
            for v in range(4):              # 4방향 탐색
                ncol = col + dcol[v]            # ncol, nrow 생성
                nrow = row + drow[v]
                if 0<=ncol<cols and 0<=nrow<rows:   # ncol, nrow 범위 주의 + arr, visited 조건 값 추가
                    visited[ncol][nrow] = 1         # 새로운 위치에서의 방문 처리
                    queue.append((ncol, nrow))      # 새로운 위치에서 탐색을 계속 할 수 있도록 queue에 삽입


def dfs():
    pass
