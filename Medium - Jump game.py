def jump(nums):
    
    n = len(nums)
    end = n - 1

    for i in range(n-2,-1,-1):
        
        if i + nums[i] >= end:
            end = i

    return end == 0


nums = [2,3,0,1,4]
print(jump(nums))