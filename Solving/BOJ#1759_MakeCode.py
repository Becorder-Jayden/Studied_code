import sys
sys.stdin = open('BOJ#1759_MakeCode.txt')

# 6개중에 4개의 값을 선택, 최소 한개의 모음이 사용되야 함
# 순열 → visited 개념 사용: 뽑은 걸 다시 뽑지 않도록 확인
''' try1: 순열 소스코드 사용 시도 → 실패 
def perm(level, temp):
    global visited
    if level == L:
        print(level, temp)
        # print(''.join(temp))
        return

    for i in range(C):
        if visited & (1<<i): continue       # arr 인덱스의 i번째 위치한 값이 이미 체크(포함) 되었을 떄 제외
        visited += 1 << i       # 1<<i번째 인덱스 체크
        perm(level+1, temp+[arr[i]])   # level+1 번째 깊이에 대해 진행
        visited -= 1 << i       # 1<<i번째 인덱스 체크 해제
'''
''' try2: N과 M(2) 풀이 이용
'''

def comb(level, start, temp):
    if level == L:
        global flag

        for i in ['a', 'e', 'i', 'o', 'u']:
            if i in temp:
                flag = True
        if flag:
            print(''.join(temp))
        return

    for s in range(start+1, C):
        print(flag)
        comb(level+1, s, temp+[code[s]])

L, C = map(int, input().split())    # L개의 소문자, C가지 암호 종류
code = sorted(input().split())
flag = False

arr = [i for i in range(C)]
visited = 0
comb(0, -1, [])


# print(arr)
# print(visited)


# print(L, C)
# print(sorted(code))



ans = ['acis','acit','aciw','acst','acsw','actw','aist','aisw','aitw','astw','cist','cisw','citw','istw']

my =  ['acis','acit','aciw','acst','acsw','actw','aist','aisw','aitw','astw','cist','cisw','citw','cstw','istw',]
print(my == ans)