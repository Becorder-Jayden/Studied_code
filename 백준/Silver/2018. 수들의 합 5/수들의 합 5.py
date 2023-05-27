N = int(input())
answer = 1      # 탐색 값이 N에 도달하면 항상 정답은 1 이상이 됨
start_idx = 1   # 초기 start_idx
end_idx = 1     # 초기 end_idx
S = 1           # 1에서부터 시작(초기 start_idx, end_idx가 갖는 S값)

while end_idx != N:     # end_idx == N이 되면 탐색 의미x
    if S == N:              # 누적합이 N과 일치
        answer += 1         # 정답 +1

        # start_idx ~ (new) end_idx 탐색
        end_idx += 1        # end 인덱스 위치 변경
        S += end_idx        # S > N 조건에 걸릴 수 있도록 S를 end_idx만큼 증가

    elif S > N:     # 누적합이 N보다 클 때
        S -= start_idx      # 기존 start_idx 값을 제거
        start_idx += 1      # start 인덱스 위치 변경

    else:  # S < N
        end_idx += 1        # end 인덱스 위치 변경
        S += end_idx        # S값 변경

print(answer)
