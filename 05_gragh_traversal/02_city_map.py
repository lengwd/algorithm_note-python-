
def read_map():
    num_cities = int(input("input num_cities: "))
    num_roads = int(input("input num_roads: "))

    arr = [[0]*num_cities for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                arr[i][j] = float("inf")

    for _ in range(num_roads):
        a = int(input("dot 1: ")) - 1
        b = int(input("dot 2: ")) - 1
        c = int(input("distance: "))
        arr[a][b] = c
        print()
        

    return arr


def main():
    # total = 0

    arr = read_map()
    w = len(arr)

    book = [0] * w

    min_dist = float("inf")

    def dfs(cur, dis):
        nonlocal min_dist
        if dis > min_dist:
            return
        if cur == 4:
            if dis < min_dist:
                min_dist = dis
            return
        
        

        for i in range(w):
            if book[i] == 0 and arr[cur][i] != float("inf"):
                book[i] = 1
                dfs(i, dis+arr[cur][i])
                book[i] = 0

    book[0] = 1
    dfs(0, 0)
    print(min_dist)


if __name__ == "__main__":
    main()