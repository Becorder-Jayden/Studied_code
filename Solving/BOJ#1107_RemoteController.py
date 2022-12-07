import sys
sys.stdin = open('BOJ#1107_RemoteController.txt')

# 풀이 전략 : 완전탐색
## 누를 수 있는 버튼 리스트에서 고장난 버튼을 제거
## 남은 숫자 버튼 리스트를 가지고 백트래킹으로 N과 가장 가까운 수 만들기
## 만들어진 수와 N과의 차이만큼 추가적으로 버튼을 누른다

# 다른 사람의 코드를 보고 리뷰

N = int(input())
M = int(input())
bkn_btn = list(map(int, input().split()))

# 현재 채널에서 +/-만 사용해서 이동하는 경우
min_cnt = abs(N-100)

for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in bkn_btn:        # 각 숫자가 고장났는지 확인하고, 고장났다면 break
            break                          # continue 보다는 break가 연산 과정을 훨씬 줄임
        elif j == len(nums)-1:           # j: nums의 자리수, len(nums)-1
            print(j, len(nums)-1)
            min_cnt = min(min_cnt, abs(int(nums)-N) + len(nums))

print(min_cnt)


# 시도 2
'''
## 백트래킹 먼저 적용 후에 고장난 번호 제거

#순열로 모든 숫자를 만드는데
#[6, 7, 8]을 포함안하고 만든 걸 하고 싶거든
def perm(level, temp):
    global visited

    if level == 4:
        numb = ''
        for i in temp:
            numb += str(i)
        print(abs(N-int(numb)))
        return

    for i in arr:
        if visited & (1 << i): continue
        visited += 1 << i
        perm(level+1, temp+[i])
        visited -= 1 << i



N = int(input())
M = int(input())
if M > 0:
    bkn_btns = list(map(int, input().split()))
else:
    bkn_btns = []

visited = 0
arr = [i for i in range(10)]
for i in bkn_btns:
    arr.remove(i)
print(arr)
print('bkn_btns:', bkn_btns)

perm(0, [])
'''


# 시도 1
'''
def perm(level, temp):
    global visited
    if level == 3:
        print(temp)
        return

    for i in range(8):
        if visited & (1<<i): continue
        visited += 1 << i
        perm(level+1, temp+[arr[i]])
        visited -= 1 << i

arr = [i for i in range(8)]
visited = 0
perm(0, [])

def mk_num(lst):
    global visited
    print('N:', N)
    print(lst)

    N_len = len(list(str(N)))       # N의 자리수
    visited = 0
    perm(0, [], N_len)

def perm(level, temp, N_len):
    global visited

    if level == N_len:
        print(temp)
        return

    for i in btn_lst:
        if visited & (1 << i): continue
        visited += 1 << i
        perm(level+1, temp+[btn_lst[i]], N_len)
        visited -= 1 << i


T = 1
for tc in range(1, T+1):
    print(f'#{tc}')
    # N: 이동하고자 하는 채널, M: 고장난 버튼의 개수, ~고장난 버튼
    N = int(input())
    M = int(input())
    if M > 0:
        bkn_btns = list(map(int, input().split()))
    else:
        bkn_btns = []
    now_channel = 100
    answer = 0

    btn_lst = [i for i in range(10)]
    for i in bkn_btns:
        btn_list[btn_lst.index(i)] = 0
        # btn_lst.replace(i, 0)

    mk_num(btn_lst)

    # print('N:', N)
    # print('M:', M)
    # print('bkn_btns:', bkn_btns)

'''