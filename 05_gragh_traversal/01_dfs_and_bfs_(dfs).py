
def read_map():
    n = int(input("input height: "))
    w = int(input("input nums: "))

    arr = [[0]*w for _ in range(w)]

    for i in range(w):
        for j in range(w):
            if i != j:
                arr[i][j] = float("inf")

    for _ in range(n):
        a = int(input("dot 1: ")) - 1
        b = int(input("dot 2: ")) - 1
        arr[a][b] = 1
        arr[b][a] = 1

    return arr



def main():
    total = 0

    arr = read_map()
    w = len(arr)

    book = [0] * w


    def dfs(cur):
        nonlocal total
        total += 1
        print(cur+1)
        if total == w:
            return
        
        for i in range(w):
            if arr[cur][i] == 1 and book[i] == 0:
                book[i] = 1
                dfs(i)
        
        return

    ## initial
    book[0] = 1
    dfs(0)

if __name__ == "__main__":
    main()