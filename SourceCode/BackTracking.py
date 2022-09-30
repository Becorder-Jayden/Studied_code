# 백트래킹
'''
해를 찾는 도중 막히면 되돌아가서 다시 해를 찾아가는 기법
상태공간트리는 백트래킹 문제의 기본
최적화 문제, 결정 문제를 해결 (결정문제 : 문제의 조건을 만족하는 해가 존재하는가를 묻는 문제)
ex) n-Queen, Map coloring, 부분집합의 합, 미로찾기
'''

N = 4
arr = [i+1 for i in range(N)]

def backtrack(k, cur_sum):   # k: 현재 노드의 높이, 함수 호출 깊이, k번 선택한 상태 등.. cur_sum 재귀호출을 진행하며 더해온 값을 저장
    if k == N:
        pass
    # 첫번째 선택 → 저장, 계산작업
    backtrack(k+1, cur_sum+arr[k])
    # 초기상태로 돌아옴, 두번재 선택
    backtrack(k+1, cur_sum)



backtrack(0)




