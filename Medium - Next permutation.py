from itertools import permutations

def next_permutation(nums):
  
    n = len(nums)

    i = n - 2
    while i>=0:
        if nums[i] < nums[i+1]: break
        else: i-=1
    print(i)
    if i>=0:
        minIndex = i+1
        min = nums[i+1]
        for j in range(i+1,n):
            if nums[j] > nums[i]: 
                if nums[j] < min: 
                    minIndex = j
                    min = nums[j]
        print(minIndex)
        nums[i],nums[minIndex] = nums[minIndex],nums[i]

        i+=1 
        j=n-1

        while i <=j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j-=1

        return nums

    i = 0
    j = n - 1

    while i <=j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j-=1



# Example usage:
original_permutation = [8,9,8,6]

print(f"Original Permutation: {original_permutation}")

next_perm = next_permutation(original_permutation)

print(f"Next Permutation: {next_perm}")
