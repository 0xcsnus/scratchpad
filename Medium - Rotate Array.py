def rotate_array(nums,k):
    
    n = len(nums)
    k = k % n

    if k != 0:

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1 


        i, j = 0, n - 1
        reverse(i,j)

        i, j = 0, k - 1
        reverse(i,j)

        i, j = k, n - 1
        reverse(i,j)


    return nums
    



nums = [1,2,3,4,5,6,7]
k = 3

result = rotate_array(nums,k)

print(result)