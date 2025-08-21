def quick_sort(nums, left, right):
    if left >= right:
        return
    
    basic = nums[left]
    i = left
    j = right

    while i != j:
        while nums[j] >= basic and i < j:
            j -= 1
        while nums[i] <= basic and i < j:
            i += 1
        
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[left] = nums[i]
    nums[i] = basic

    quick_sort(nums, left, i-1)
    quick_sort(nums, i+1, right)


def main():
    data = input().split()
    nums = [int(x) for x in data]

    quick_sort(nums, 0, len(nums)-1)

    print(nums[0], end=" ")
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            print(nums[i], end=" ")

if __name__ == "__main__":
    main()
        
