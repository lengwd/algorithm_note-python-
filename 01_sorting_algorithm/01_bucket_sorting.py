m = int(input())
n = int(input())
data = input().split()
nums = [int(x) for x in data]

buckets = [0 for _ in range(m+1)]

for num in nums:
    buckets[num] += 1
for i in range(m+1):
    if buckets[i] != 0:
        for j in range(buckets[i]):
            print(i, end=" ")




