def solulu(nums):

    n = len(nums)
    if n == 1: return 0
    for i in range(0,n):
        if i == 0 and nums[i] > nums[i+1]: return i
        elif i == n - 1 and nums[i] > nums[i-1]: return n - 1
        elif nums[i] > nums[i-1] and nums[i] > nums[i+1]: return i

    return -1 

def solution(nums):

    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (left+right) // 2
        if nums[mid] >= nums[mid+1]: right = mid
        else: left = mid + 1

    return left





print(solution([1,2,1,3,5,6,4]))