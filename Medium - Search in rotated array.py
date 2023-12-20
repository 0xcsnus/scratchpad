'''
Essentially, you are rotating it k times to the right.
if we rotate it back, it will take us O(k)

but we can not do it directly because we don't have k, so we need to find k
we need to find the pair in which first element is greater than the second element

there we have our k
now rotate it back and apply binary search

this will take O(n).

'''

def bSearch(nums,target):
    n = len(nums)
    k = 0

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            k = (i + 1) % n
            break

    def reverse(i,j):
        while i < j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j-=1
    
    reverse(0,k-1)
    reverse(k,n-1)
    reverse(0,n-1)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            if k == 0: return mid
            else: return (mid + k )%n
        elif target > nums[mid]: left = mid + 1
        else: right = mid - 1

    return -1
    

nums = [3,1]
target = 1
result = bSearch(nums,target)
print(result)