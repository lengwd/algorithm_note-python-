def main():
    s = input()
    l = len(s)

    # for
    # 关于中间的讨论
    # 奇数：len = 3 len // 2 = 1 对应的刚好是中间
    # 反之： len = 4 len // 2 = 2 对应的是中间偏一位
    # 所以 存储的时候找 <mid , 比较的时候 奇数mid+1 , 数 mid

    stack = ""
    mid = l // 2

    stack += s[:mid]
    top = len(stack) - 1
    
    if l % 2 == 0:
        begin = mid
    else:
        begin = mid + 1
    
    flag = 1
    for i in range(begin, l):
        if stack[top] != s[i]:
            
            flag = 0
            break
        top -= 1
    
    if flag:
        print("yes")
    else:
        print("no")
    

if __name__ == "__main__":
    main() 