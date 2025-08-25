game_map = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
]

def main():
    p = int(input("input label x: "))
    q = int(input("input label y: "))
    x_init = int(input("input x init: "))
    y_init = int(input("input y init: "))
    

    m = len(game_map)
    n = len(game_map[0])
    min_steps = float("inf")

    book = [[0] * n for _ in range(m)]

    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    def dfs(x, y, step):
        nonlocal min_steps

        if x == p and q == y:
            if step < min_steps:
                min_steps = step
            
            return
        
        if step > min_steps:
            return
        
        for direction in directions:
            
            tx = x + direction[0]
            ty = y + direction[1]

            if tx < 0 or tx >= m  or ty < 0 or ty >= n:
                continue

            if book[tx][ty] !=1 and game_map[tx][ty] != 1:
                book[tx][ty] = 1

                dfs(tx, ty, step+1)
                book[tx][ty] = 0

            
    
    
    book[x_init][y_init] = 1
    dfs(x_init, y_init, 0)

    print(f"min steps: {min_steps}")


if __name__ == "__main__":
    main()