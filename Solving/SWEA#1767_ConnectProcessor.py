import sys
sys.stdin = open('SWEA#1767_ConnectProcessor.txt')

dcol = [-1, 1, 0, 0, 0]
drow = [0, 0, -1, 1, 0]

# == 현재 시도 중인 과정 ==
# 프로세서가 한 방향으로 끝까지 탐색했을 때 다른 프로세서의 탐색 진행
# 메인 함수가 무엇일까? 1) 프로세서 탐색, 2) pc_lst 안의 프로세서 선택
# 부분집합으로 n개의 프로세서를 선택하는 과정이 필요하다?



# == 마친 과정 ==
# 0. 모든 프로세서의 위치 탐색, 고유 번호 붙이기 
# 1. 프로세서 한방향 탐색, 되돌아오기


# == 동민 advise ==
# 왜 완전탐색? : 프로세서 '탐색 순서'에 따라 결과가 달라지므로 모든 순서에 대해 탐색이 필요하다 → 순서
# 뽑아올 정보? : 좌표(arr 상의 1~7)번, 4 방향에 대해 탐색 (대기)
# 탐색할 것 : pc_lst 안에 있는 프로세서들
# 깊이(레벨): 바뀐 프로세서의 위치

# 나(경민)이 시도하는 방법은 종료조건이 명확하게 인식되지 않아서 고민이 많아질 듯. 다시 시작점을 생각해보기
# pc_lst를 가지고 백트래킹 시도

# cur_sum : 함수의 매개변수로 원하는 정보를 넣어버림

# 하나의 프로세서 탐색 함수 : 프로세서 위치, 방향이 주어졌을 때,
# → 프로세서 탐색 함수에서 전진, 후퇴가 동시에 일어나도록 시도
def exp_proc_vec(col, row, v):      # 구현(백트래킹이 2번까지는 잘 안들어감, 보통 메인 함수를 백트래킹으로 사용하곤 함)
    d = 0

    # if col == 0 or row == 0:        # 프로세서의 연결이 완료 → 다음 프로세서 탐색 필요
    #     return d
    while True:
        d += 1
        ncol = col + dcol[v] * d
        nrow = row + drow[v] * d
        if 0<=ncol<N and 0<=nrow<N and arr[ncol][nrow] == 0:
            arr[ncol][nrow] = arr[col][row]
            # exp_proc_vec(ncol, nrow, v)
        else:
            return d
            # break
    # return d
def reset_proc_vec(col, row, v, d):
    if col == 0 or row == 0:
        return

    for i in range(1, d):
        ncol = col + dcol[v] * i
        nrow = row + drow[v] * i
        if 0 <= ncol < N and 0 <= nrow < N: #and copy_arr[ncol][nrow] == 0 and arr[ncol][nrow] == arr[col][row]:
            arr[ncol][nrow] = 0
            # reset_proc_vec(ncol, nrow, v, d)


# 백트래킹 생성: pc_lst 요소를 가지고 탐색할 수 있도록
def backtrack(level, temp):
    # 6이 아니라 7이 되는것이 좋은 이유 : 종료 조건에는 종료에 해당할 수 있는 요소로 가리키기 → len(pc_lst)로 변경
    # 마지막 깊이에 도달했을 때도 탐색이 이뤄져야 함
    if level == len(pc_lst):
        global max_connect, answer
        temp_connect = 0            # 현재 연결된 프로세서의 수
        line_cnt = 0                # 전선(+ 프로세서)의 수
        connect_proc = []
        for col in range(N):
            for row in range(N):
                if (col == 0 or row == 0 or col == N-1 or row == N-1) and arr[col][row]:
                    temp_connect += 1
                if arr[col][row]:
                    line_cnt += 1
                # if (col == 0 or row == 0 or col == N-1 or row == N-1) and arr[col][row]:
                #     connect_proc.append(arr[col][row])


        #
        # cnt = 0
        # ans = 0
        # for col in range(N):
        #     for row in range(N):
        #         if arr[col][row] in connect_proc:
        #             cnt += 1



        #
        #         if (col == 0 or row == 0 or col == N or row == N) and arr[col][row]:
        #             connected_proccesor.append(arr[col][row])
        #
        # print(connected_proccesor)
        #
        # side_prec = 0
        # for col in range(N):
        #     for row in range(N):
        #         if arr[col][row] in connected_proccesor:
        #             test_cnt += 1
        #
        #
        # print('test_cnt:', test_cnt)


                #


        # (이전에 찾은) 최대 연결 프로세서보다 더 많은 프로세서가 연결 되었을 경우
        if max_connect < temp_connect:
            max_connect = temp_connect
            answer = line_cnt - temp_connect        # line_cnt - temp_connect: (프로세서를 제외한 전선만의 길이)

            # for i in arr:
            #     print(i)
            # print('answer:', answer)

        # (이전에 찾은) 최대 연결 프로세서와 같은 수의 프로세스가 연결되었을 때
        elif max_connect == temp_connect:
            if line_cnt - temp_connect < answer:
                answer = line_cnt - temp_connect



        return

    # 여기에 탐색 함수 작성
    for v in range(5):
        # 만들어낼 정보

        repeat = exp_proc_vec(pc_lst[level][0], pc_lst[level][1], v)

        backtrack(level+1, temp+[lst[level]])

        # 초기화 할 정보
        reset_proc_vec(pc_lst[level][0], pc_lst[level][1], v, repeat)



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    copy_arr = [arr[i][:] for i in range(len(arr))]
    pc_lst = []
    max_connect = 0
    answer = 0xffff

    num = 1
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 1:
                if col != 0 and row != 0 and col != N-1 and row != N-1:
                    pc_lst.append((col, row))
                    arr[col][row] = num
                    num += 1

    print('pc_lst:', pc_lst)
    # (1, 2) 프로세서 기준 탐색 시도
    # for c, r in pc_lst:
    # for v in range(4):
    #     exp_proc_vec(1, 2, v)

    # subset(0, [], pc_lst)

    lst = [i for i in range(len(pc_lst))]
    backtrack(0, [])

    # print(max_connect)

    # for i in arr:
    #     print(i)
    # print()
    # cnt = 0
    # for col in range(N):
    #     for row in range(N):
    #         if arr[col][row]:
    #             if col != 0 and row != 0:
    #                 cnt += 1
    # print('cnt:', cnt)
    print(f'#{tc}','======================', answer)