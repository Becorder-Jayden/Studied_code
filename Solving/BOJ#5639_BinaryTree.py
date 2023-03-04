import sys
sys.stdin = open("BOJ#5639_BinaryTree.txt")

def postorder(left, right):    # 전위순행 -> 후위순행
    if left > right:    # 왼쪽 노드가 오른쪽 노드보다 작거나 같을 때만 진행할 수 있도록 함
        return
    mid = right + 1  # 오른쪽 노드가 없을 경우???

    for i in range(left + 1, right + 1):
        if nums[left] < nums[i]:
            mid = i     # mid 값을 설정
            break

    postorder(left + 1, mid - 1)  # 왼쪽 확인
    postorder(mid, right)  # 오른쪽 확인
    print(nums[left])





# 전위순회의 결과가 주어짐
nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

print(nums)



postorder(0, len(nums)-1)     #가장 첫번째와 가장 마지막 인덱스 비교
