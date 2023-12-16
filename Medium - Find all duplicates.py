def duplicates_brute(nums):
    nums.sort()

    res = set()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            res.add(nums[i])
    
    return list(res)


def duplicates(nums):

    n = len(nums)
    res = []

    for i in range(n):
        while  nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1],  nums[i] =  nums[i], nums[nums[i]-1]

        
    for i in range(n):
        if i != nums[i] - 1:
            res.append(nums[i])

    return res




nums = [4,3,2,7,8,2,3,1]

print(duplicates(nums))