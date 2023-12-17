def moveZeroes(nums):
    
    index = 0

    for num in nums:
       
        if num != 0:
            nums[index] = num 
            index += 1

    for i in range(index, len(nums)):
        nums[i] = 0

    print(nums)

nums = [0,0,0,3,12]
Output = [1,3,12,0,0]

moveZeroes(nums)