# 这一章是这数最核心的一章
# 1. 首先是深度优先搜素


def main():
    n = int(input("input a number:"))
    a = [0] * (n+1)
    book = [0 for _ in range(n+1)] #book[i]=0代表i还在 book[i]=1代表不在
    count = 0
    def dfs(step, n):
        nonlocal count
        if step == n+1:
            print(a[1:])
            count += 1
            return
        
        for i in range(1, n+1):
            if book[i] == 1:
                continue
            
            a[step] = i
            book[i] = 1
            dfs(step+1, n)
            book[i] = 0

    dfs(1, n)
    print(f"count: {count}")


if __name__ == "__main__":
    main()
