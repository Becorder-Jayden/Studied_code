import sys
sys.stdin = open('input.txt')

def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
    if l[-1] > r[-1]:
        cnt += 1

    ret = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            ret.append(l[i])
            i += 1
        elif l[i] > r[j]:
            ret.append(r[j])
            j += 1

    if l: ret += l[i:]
    if r: ret += r[j:]

    return ret

ans_lst = []                # for문에서 print에 사용되는 메모리 낭비 줄이기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0

    ans_lst.append(f'#{tc} {merge_sort(a)[N//2]} {cnt}')

print('\n'.join(ans_lst))

