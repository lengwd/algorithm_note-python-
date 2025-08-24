def permute(nums, path, used, res):
    if len(nums) == len(path):
        res.append(path[:])
        return
    
    for i in range(len(nums)):
        if not used[i]:
            path.append(nums[i])
            used[i] = True
            permute(nums, path, used, res)
            path.pop()
            used[i] = False
    return res

def main():
    m = int(input("Input the number:"))
    nums = [x for x in range(1, m+1)]
    used = [False] * m
    result = permute(nums, [], used, [])

    for item in result:
        print(item)

    print(f"numbers of permutation is: {len(result)}")

if __name__ == "__main__":
    main()