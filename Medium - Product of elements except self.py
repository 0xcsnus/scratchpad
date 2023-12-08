def solulu(nums):

    n = len(nums)

    left, right, result = [], [], []

    for num in nums:
        if not left: left.append(num)
        else: left.append(num*left[-1])
    
    for num in reversed(nums):
        if not right: right.append(num)
        else: right.append(num*right[-1])

    right = list(reversed(right))

    for i in range(n):

        if i == 0: result.append(right[i+1])
        elif i == n - 1: result.append(left[n-2])
        else: result.append(left[i-1]*right[i+1])

    return result

nums = [1,2,3,4]
print(solulu(nums))