def solulu(nums):
    if not nums: return 0

    n = len(nums)

    localSum = globalSum = nums[0]
    
    for i in range(1,n):

        localSum = max(localSum+nums[i],nums[i])
        globalSum = max(localSum,globalSum)

    return globalSum



nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solulu(nums))