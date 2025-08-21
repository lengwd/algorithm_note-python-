data = input().split()
nums = [int(x) for x in data]


def quick_sort(nums, left, right):
    if left >= right:
        return 
    
    temp = nums[left]
    i = left
    j = right

    while i != j:
        while nums[j] >= temp and i < j:
            j -= 1
        while nums[i] <= temp and i < j:
            i += 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[left] = nums[i]
    nums[i] = temp

    left = quick_sort(nums, left, i-1)
    right = quick_sort(nums, i+1, right)
    

quick_sort(nums, 0, len(nums)-1)

for num in nums:
    print(num, end=" ")
