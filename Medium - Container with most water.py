def maxWater(height):
    
    n = len(height)
    left, right, max_water = 0, n - 1, 0

    while left < right:

        width = right - left
        retention = width * min(height[left],height[right])
        max_water = max(retention,max_water)

        if height[left] < height[right]: left+=1
        else: right -= 1

    return max_water

nums = [1,8,6,2,5,4,8,3,7]

result = maxWater(nums)

print(result)