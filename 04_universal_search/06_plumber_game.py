game_map = [
    [5, 3, 5, 3],
    [1, 5, 3, 0],
    [2, 3, 5, 1],
    [6, 1, 1, 5],
    [1, 5, 5, 4]
]

def main():

    x_init = int(input("input x init: ")) - 1
    y_init = int(input("input y init: ")) - 1
    

    m = len(game_map)
    n = len(game_map[0])

    book = [[0]*n for _ in range(m)]
    flag = 0
    path = []
    def dfs(x: int, y: int, font: int):
        nonlocal flag
        # font 代表 入水口方向 1 2 3 4 分别代表上下左右
        if x == m-1 and y == n:
            flag = 1
            print("find path: ")
            print(path)

        if x < 0 or x >= m or y < 0 or y >= n:
            return
        
        if book[x][y] == 1:
            return
        
        book[x][y] = 1
        path.append((x+1, y+1))

        if game_map[x][y] in [5, 6]: ## 直水管
            if font == 1:
                dfs(x, y+1, 1)
            elif font == 2:
                dfs(x+1, y, 2)
            elif font == 3:
                dfs(x, y-1, 3)
            elif font == 4:
                dfs(x-1, y, 4)
            else:
                print("font is wrong")
        
        if game_map[x][y] in [1, 2, 3, 4]:
            if font == 1:
                dfs(x+1, y, 2)
                dfs(x-1, y, 4)
            elif font == 2:
                dfs(x, y+1, 1)
                dfs(x, y-1, 3)
            elif font == 3:
                dfs(x+1, y, 2)
                dfs(x-1, y, 4)
            elif font == 4:
                dfs(x, y+1, 1)
                dfs(x, y-1, 3)
            else:
                print("font is wrong")
        
        book[x][y] = 0
        path.pop()

    dfs(x_init, y_init, 1)
                
if __name__ == "__main__":
    main()
