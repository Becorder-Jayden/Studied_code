# 이차원 딥카피 연습:

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
copy_arr = [arr[i][:] for i in range(len(arr))]

# 슬라이싱을 이용한 깊은 복사
# arr의 i열에 대해서 행을 복사
copy_arr = [arr[i][:] for i in range(N)]

# 조합을 이용한 완전탐색
def comb(level, start, temp)
	if level == 3:	# 목표했던 깊이에 도달했을 때
		# 원하는 작업에 대한 코드 입력
        return		# 이전 깊이로 return

	# start+1: 한번 선택한 인덱스(start)를 다시 뽑지 않고 이후의 인덱스를(start+1) 탐색하도록 함
	# len(possible): 벽을 세울 수 있는 모든 범위
    for s in range(start+1, len(possible)):
    	# 깊이를 1 증가, start+1 ~ len(possible) 범위의 값(possible[s])를 temp 공간에 append 하고 dfs 진행
    	comb(level+1, s, temp+[possible[s]])