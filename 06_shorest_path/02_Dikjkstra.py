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

    # 步骤1 先dis 存储到 1点的距离
    # 2： 找到dis 中最小的值 再用 最小值 最小值作为中介来跟新 dis

    book  = [0] * length # 用于存储是否已经用于松弛

    # 初始
    dis = arr[0][:]
    book[0] = 1


    for _ in range(length-1):
        min_dis = float("inf")
        min_idx = None
        for i in range(length):
            if book[i] == 0 and dis[i] < min_dis:
                min_dis = dis[i]
                min_idx = i
                
        book[min_idx] = 1
        for k in range(length):
            if book[k] == 0 and dis[min_idx] + arr[min_idx][k] < dis[k]:
                dis[k] = dis[min_idx] + arr[min_idx][k]

    print(dis)


# 这里犯了两个错误 ： 一个没有修改book 另一个没有松弛之后的值来做判据

if __name__ == "__main__":
    main()