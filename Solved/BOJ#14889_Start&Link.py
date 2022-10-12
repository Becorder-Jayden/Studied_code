import sys
sys.stdin = open('BOJ#14889_Start&Link.txt')

# 시간이 오래 걸리는거 빼면 괜찮은 풀이인듯..

def make_score(lst):
    score = 0
    for i in lst:
        for j in lst:
            if i != j:
                score += team[i][j]
    return score


def comb(level, start, temp):
    if level == N//2:
        set_A, set_B = set(temp), set(arr)-set(temp)
        li_A.append(set_A)
        li_B.append(set_B)
        return
    for i in range(start+1, N):
        comb(level+1, i, temp+[arr[i]])


N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]
answer = 0xffff
arr = [i for i in range(N)]
li_A = []
li_B = []

comb(0, -1, [])

for i in range(len(li_A)):
    answer = min(answer, abs(make_score(li_A[i]) - make_score(li_B[i])))

print(answer)
