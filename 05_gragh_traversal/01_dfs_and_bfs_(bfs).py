
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
    # total = 0

    arr = read_map()
    w = len(arr)

    book = [0] * w
    queue = [0] * (w+1) 

    head = 0 
    tail = 0
    
    book[tail] = 1
    queue[tail] =  1
    print(0+1)
    tail += 1

    while head < tail:
        for i in range(w):
            if arr[head][i] == 1 and book[i] ==0:
                book[i] = 1
                print(i+1)
                queue[tail] = i
                tail += 1
        head += 1

    print(f"queue: {queue}")


if __name__ == "__main__":
    main()