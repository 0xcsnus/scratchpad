def threeSum(nums):
    n = len(nums)
    nums.sort()
    res = set()
    i = 1
    while i < n - 2:

        if i > 0 and nums[i] == nums[i-1]: i+=1

        j = i + 1
        k = n - 1

        while j < k:

            sum = nums[i] + nums[j] + nums[k]
            if sum == 0: 
                res.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
            elif sum > 0:
                k-=1
            else: j+=1

        i+=1

    return [list(x) for x in res]


nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))