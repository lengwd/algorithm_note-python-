game_map = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
]

class Queue:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.f = None
        self.step = 0

def main():
    p = int(input("input label x: "))
    q = int(input("input label y: "))
    x_init = int(input("input x init: "))
    y_init = int(input("input y init: "))
    
    

    m = len(game_map)
    n = len(game_map[0])

    notes = [Queue() for _ in range(m*n + 11)]

    book = [[0]*n for _ in range(m)]

    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    # 初始化
    book[x_init][y_init] = 1
    head = 0
    tail = 1
    notes[head].x = x_init
    notes[head].y = y_init
    notes[head].f = None
    notes[head].step = 0

    found = False

    

    while head < tail and not found:
        for direction in directions:
            tx = notes[head].x + direction[0]
            ty = notes[head].y + direction[1]

            if tx < 0 or tx >= m or ty < 0 or ty >= n:
                continue

            if book[tx][ty] == 0 and game_map[tx][ty] == 0:
                book[tx][ty] = 1
                notes[tail].x = tx
                notes[tail].y = ty
                notes[tail].f = notes[head]
                notes[tail].step = notes[head].step + 1
                tail += 1

                if tx == p and ty == q:
                    
                    found = True
                    print(notes[head].step + 1)
                    
                    break
        
        head += 1
                
if __name__ == "__main__":
    main()