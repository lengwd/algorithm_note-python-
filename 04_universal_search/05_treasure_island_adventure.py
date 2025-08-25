game_map = [
    [1, 2, 1, 0, 0, 0, 0, 0, 2, 3],
    [3, 0, 2, 0, 1, 2, 1, 0, 1, 2],
    [4, 0, 1, 0, 1, 2, 3, 2, 0, 1],
    [3, 2, 0, 0, 0, 1, 2, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 5, 3, 0],
    [0, 1, 2, 1, 0, 1, 5, 4, 3, 0],
    [0, 1, 2, 3, 1, 3, 6, 2, 1, 0],
    [0, 0, 3, 4, 8, 9, 7, 5, 0, 0],
    [0, 0, 0, 3, 7, 8, 6, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

class Queue:
    def __init__(self):
        self.x = None
        self.y = None
        



def main():
   
    x_init = int(input("input x init: ")) - 1
    y_init = int(input("input y init: ")) - 1

    m = len(game_map)
    n = len(game_map[0])

    book = [[0]*n for _ in range(m)]
    notes = [Queue() for _ in range(m*n + 1)]

    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    total_count = 0

    # 初始化
    head = 0
    tail = 0

    if game_map[x_init][y_init] == 0:
        print("little ha is unlucky, birth in the sea")
        return
    
    book[x_init][y_init] = 1
    notes[tail].x = x_init
    notes[tail].y = y_init
    total_count += 1

    tail += 1

    while head < tail:
        for direction in directions:
            tx = notes[head].x + direction[0]
            ty = notes[head].y + direction[1]

            if tx < 0 or tx > m or ty < 0 or ty > n:
                continue

            if book[tx][ty] == 0 and game_map[tx][ty] != 0:
                total_count += 1
                book[tx][ty] = 1
                notes[tail].x = tx
                notes[tail].y = ty
                tail += 1
        
        head += 1

    print(f"island size: {total_count}")
### 也可用dfs来完成 但是注意 book不用撤销 因为每个地方只计算一次


if __name__ == "__main__":
    main()