def solulu(nums):
    result = nums[0]
    for i in range(1,len(nums)):
        result ^= nums[i]

    return result


print(solulu([1,1,2,2,3,3,4]))