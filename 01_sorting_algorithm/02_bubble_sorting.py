m = int(input())
n = int(input())
data = input().split()
nums = [int(x) for x in data]

for i in range(n-1):
    for j in range(n-1-i):
        if nums[j] < nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

for num in nums:
    print(num, end=" ")