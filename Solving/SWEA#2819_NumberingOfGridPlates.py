import sys
sys.stdin = open('input.txt')

# 정답은 맞췄지만 시간이 너무 오래걸림
# 수민's help : 재귀 함수의 순서를 바꾸어서 해결
# + 종료조건을 앞으로 두는 함수의 꼴을 맞춰주기 위해서 함수 시작전 초기값을 넣어주고, 함수를 호출하면서 추가적인 작업을 진행

# * 저장된 값을 변수명으로 넘겼더니 속도가 1/10로 줄어들었다.


dcol = [1, -1, 0, 0]
drow = [0, 0, -1, 1]

def f(col, row, move, make):
    if len(make) == 7:
        ans_li.append(make)                 # 재귀함수를 호출하며 만든 make를 ans_li에 저장
        return

    for v in range(4):                      # 4방향 탐색을 진행하면서 경로값을 추가
        ncol = col + dcol[v]
        nrow = row + drow[v]
        if move and 0<=ncol<4 and 0<=nrow<4:
            f(ncol, nrow, move-1, make + str(arr[ncol][nrow]))


for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans_li = []
    for col in range(4):                            # arr 안의 모든 시작점을 대상으로 진행
        for row in range(4):
            f(col, row, 7, str(arr[col][row]))
    print(f'#{tc} {len(set(ans_li))}')


