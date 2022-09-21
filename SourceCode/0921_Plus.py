# point 가능한 모든 경우를 처리해서 정답을 추정(시간초과 발생 가능)
'''
백트래킹의 대원칙 : 모든 경우의 수를 탐색하면 정답이 나온다
* 정답은 **종료시에 처리(가지치기는 마지막 단계에서), 효율적으로 생각하려다 망치는 경우 다수
* 필요하면 파라미터를 최대한 만들어 사용
* 가능하면 다중트리보다는 이진트리가 좋음

1. n은 배열의 인덱스 → n을 종료 조건과 관련되도록 사용
def dfs(n, S)
    # 종료조건: n에 관련
    if n == N:
        정답 관련 처리!
        return
    # 하부함수 호출
    dfs(n+1, S)
    * 이진트리 → 1인경우 / 0인경우로 나누어 전개
    * 다중트리 → for문으로 호출
'''

# 4837. 부분집합의 합
# def dfs(n, sm, cnt):
#     global ans
#     # 가지치기 예: 진행해도 더이상 의미 없을 경우 중단
#     if K < sm:
#         return
#
#     if n == N:
#         if sm == K and cnt == CNT:
#             ans += 1
#         return
#
#     dfs(n+1, sm+lst[n], cnt+1)  # 사용하는 경우
#     dfs(n+1, sm, cnt)   # 사용하지 않는 경우
#
#
# T = int(input())
# for tc in range(1, T+1):
#     CNT, K = map(int, input().split())
#     lst = [n for n in range(1, 13)]
#     N = len(lst)
#
#     ans = 0
#     dfs(0, 0, 0)
#
#     print(f'#{tc} {ans}')
'''
input
3
3 6
5 15
5 10

print
#1 1
#2 1
#3 0
'''



'''
* 기준값으로 일반화를 시키기(N-1(or N)번째 까지)
* 가지치기는 답을 구하고 시간초과를 해결하기 위해서 사용하는 것
* 멀티트리는 N<=15를 마지노선으로 생각할 것, A형 출제 이후 15이상 넘어간 적 없음
* 이진트리는 N<=50를 마지노선으로 생각, 범위가 초과할 경우 그리디나 다른 방식을 생각해봐야 함 

n: 행 번호
dfs(n, sm,  )
    if n==N:
        if ans > sm:
            ans = sm
        return
    for j (0, N):
        if not v[j]:
            v[j] = 1
            dfs(n+1, sm+arr[n][j], )
            v[j] = 0          # 반드시 체크 사항을 변경하는것 주의
'''
# 배열 최소 합
# used 사용 ← 가능한 모든 경우를 처리하는 것이 백트래킹

# def dfs(n, sm):
#     global ans
#     if n == N:
#         if ans > sm:            # 가지치기
#             ans = sm
#         return
#
#     for j in range(N):
#         if not v[j]:
#             v[j] = 1
#             dfs(n+1, sm+arr[n][j])
#             v[j] = 0            # 잊지말자 clear!
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 10*N      # 최소값을 구할 경우, 초기값은 최대치
#     v = [0] * N
#     dfs(0, 0)
#
#     print(f'#{tc} {ans}')



'''
제약사항 등을 통해 백트래킹 문제임을 확인할 수 있어야 함
추가조건 : n회에 lst를 이미 만들어봤다면 가지치기
* 리스트로 만들면 상대적으로 오래걸린다
* 딕셔너리로 만들면 빠름

- 하부함수 호출 L에서 2개 뽑는 가능한 모든 조합
for i (L-1):
    for j (i+1, L):
        lst[i] lst[j] 교환
        dfs(n+1, )
        lst[i] lst[j] 교환 → 원상복구
- 종료조건
if n == N:
    ans = max(ans, lst숫자화)
    return
'''
# 최대 상금
def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int(''.join(map(str, lst))))
        return
    
    for i in range(L-1):
        for j in range(i+1, L):     # L개에서 2개 뽑기
            cst = ''.join(map(str, lst))
            if (n, cst) not in v:       # 방문 안한 경우
                lst[i], lst[j] = lst[j], lst[i]
                dfs(n+1)
                v.append((n, cst))
                lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T+1):
    st, t = input().split()
    N = int(t)
    lst = []
    for ch in st:
        lst.append(int(ch))

    L = len(lst)
    ans = 0     # 최대값
    dfs(0)
    
    print(f'#{tc}')