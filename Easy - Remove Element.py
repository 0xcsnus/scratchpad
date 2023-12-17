def remove(nums,val):
    left, right, k = 0, len(nums) - 1, 0

    while left <= right:

        while left<=right and nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            
        if left <= right:
            k += 1
            left += 1

    return k


nums = [1]
val = 1
print(remove(nums,val))