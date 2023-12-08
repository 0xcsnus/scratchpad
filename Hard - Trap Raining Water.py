def solulu(nums):

    n = len(height)

    left, right = [0]*n, [0]*n

    left[0] = height[0]
    right[n-1] = height[n-1]

    for i in range(1,n):
        left[i] = max(left[i-1],height[i])

    for i in range(n-2,-1,-1):
        right[i]  = max(right[i+1],height[i])

    retention = 0

    for i in range(n):
        retention += min(left[i],right[i]) - height[i]

    return retention




height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solulu(height))