import sys
sys.stdin = open('SWEA#14510_TreeHeight.txt')

# A형 문제_부분정답 42/50
# sum으로 중간값을 뭉개버리면 안됨.

# 1
# 6
# 2 2 2 4 4 5

# 1
# 3
# 4 4 5

#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     arr.sort(reverse=True)
#     M_height = arr[0]
#
#     diff_arr = []
#     for i in arr:
#         diff_arr.append(M_height-i)
#
#     if sum(diff_arr) == False:
#         print(f'#{tc} {0}')
#         continue
#
#     three = 0
#     one = 0
#     two = 0
#     for i in range(N):
#         if diff_arr[i] >= 3:
#             three += diff_arr[i]//3
#             diff_arr[i] = diff_arr[i]%3
#         if diff_arr[i] == 1:
#             one += 1
#         elif diff_arr[i] == 2:
#             two += 1
#
#     same_min = min(one, two)
#     if same_min > 0:
#         three += same_min
#         one -= same_min
#         two -= same_min
#
#     One = Two = 0
#     for i in diff_arr:
#         if i == 1:
#             One += 1
#         elif i == 2:
#             Two += 1
#
#     # print(One, Two)
#     One, Two = One - min(One, Two), Two - min(One, Two)
#     # print(three, One, Two)
#     answer = three*2
#     if One:
#         answer += 2*One - 1
#     elif Two:
#         if Two%3 == 0:
#             answer += Two//3
#         elif Two%3 == 1:
#             answer += Two//3 + 2
#         elif Two%3 == 2:
#             answer += 4
#     if tc == 6:
#         print(three, diff_arr, One, Two)
#         print(f'#{tc} {answer}')



# 승환 풀이
for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    Big = max(arr)
    total = 0
    one = 0
    for i in range(N):
        total += Big - arr[i]           # total: 가장 높은 나무와 각 나무 높이의 차이
        if (Big - arr[i]) % 2:          # 만약 (가장 큰 높이 - 어떤 나무의 높이)가 홀수라면 one += 1
            one += 1

    # print('total:', total, 'one:', one, 'two:', total-one)

    # one의 개수가 더 많을 때: 3일짜리 세트가 반복되어야 함, 가장 처음 1은 곧바로 실행되므로 1을 빼줌
    if one * 3 > total:
        print(f'#{t}', one * 2 - 1)

    # one의 개수가 더 적거나 같을 때:
    else:
        total -= one * 3
        # print('total', total)
        print(f'#{t}', one * 2 + (total // 3) * 2 + (total % 3))







# 오답 42/50
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_arr = max(arr)
#     answers = 0
#
#     diff_arr = []
#     for i in arr:
#         if max_arr-i != 0:
#             diff_arr.append(max_arr - i)
#
#     diff_arr.sort()
#     # print(diff_arr)
#
#     if sum(diff_arr) == 0:
#         answer = 0
#         print(f'#{tc} {answer}')
#         continue
#
#     total_diff = sum(diff_arr)
#     OT, residue = total_diff//3, total_diff%3
#
#     print(total_diff)
#     print(OT, residue)
#
#     answer = OT*2
#     if residue == 1:
#         answer += 1
#     elif residue == 2:
#         print(diff_arr)
#
#
#
#     print(f'#{tc} {answer}')