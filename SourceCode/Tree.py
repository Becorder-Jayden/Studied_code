V = 13
E = V-1        # 정점수 간선수
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

P = [0] * (V+1)
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
	p, c = arr[i*2], arr[i*2+1]
	if ch1[p] == 0:
		ch1[p] = c
	else:
		ch2[p] = c

print(P)
print(ch1)
print(ch2)

def find_root(V):
	for i in range(1, V+1):
		if arr[i] == 0:
			return i

# 트리의 높이를 계산
def tree_height(v):
	if v == 0: return -1
	lh = tree_height(L[v])
	rh = tree_height(R[v])
	return max(lh, rh) + 1

print(tree_height(1))
print(tree_height(3))



cnt = 0
def tree_size(v):
	if v == 0: return 0
	l = tree_size(L[v])
	r = tree_size(R[v])
	return l + r + 1

print(tree_size(3))


# 높이가 n인 노드들 찾기
def find_common_height(n):
	pass

# v번 노드가 루트인 트리의 전체 노드 수를 계산
def find_node_cnt(v):
	pass

# v1, v2 노드의 공통 조상 찾기
def find_common_ancesstor(v1, v2):
	pass