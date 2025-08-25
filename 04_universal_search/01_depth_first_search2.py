# 这个代码是解决第四章第一节的第二个问题
# ()()() + ()()() = ()()()




def main():
    a = [0] * 9 # 作为这9个数字的容器
    book = [0] * 9 # 用于记录这个数字是否使用
    count = 0
    def dfs(step):
        nonlocal count
        # nonlocal book
        if sum(book) == 9:
            left1 = a[0]*100 + a[1]*10 + a[2]
            left2 = a[3]*100 + a[4]*10 + a[5]
            right = a[6]*100 + a[7]*10 + a[8]
            if left1 + left2 == right:
                count += 1
                print(f"{a[0]}{a[1]}{a[2]}+{a[3]}{a[4]}{a[5]}={a[6]}{a[7]}{a[8]}")
            return
        
        for i in range(9):
            if book[i] == 1:
                continue
            
            book[i] = 1
            a[step] = i + 1
            dfs(step+1)
            book[i] = 0 
    dfs(0)
    print(f"count: {count//2}")

if __name__ == "__main__":
    main()
