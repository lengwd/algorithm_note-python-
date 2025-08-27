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
        # arr[b][a] = 1
        print()

    return arr


def main():
    arr = read_map()

    length = len(arr)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                if arr[i][k] < float("inf") and arr[k][j] < float("inf") and arr[i][k] + arr[k][j] < arr[i][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]

    for line in arr:
        print(line)

if __name__ == "__main__":
    main()