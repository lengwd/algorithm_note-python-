game_map = [
    "#############",
    "#GG.GGG#GGG.#",
    "###.#G#G#G#G#",
    "#.......#..G#",
    "#G#.###.#G#G#",
    "#GG.GGG.#.GG#",
    "#G#.#G#.#.###",
    "##G...G.....#",
    "#G#.#G###.#G#",
    "#...G#GGG.GG#",
    "#G#.#G#G#.#G#",
    "#GG.GGG#G.GG#",
    "#############"
] 


class Notes:
    def __init__(self):
        self.x = None
        self.y = None

def count_scores(x, y, game_map):
    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]
    scores = 0

    for direction in directions:
        tx = x
        ty = y

        while game_map[tx][ty] != '#':
            tx += direction[0]
            ty += direction[1]
            if game_map[tx][ty] == "G":
                scores += 1

    return scores

def main():
    # p = int(input("input label x: "))
    # q = int(input("input label y: "))
    x_init = int(input("input x init: "))
    y_init = int(input("input y init: "))
    
    m = len(game_map)
    n = len(game_map[0])
    notes = [Notes() for _ in range(m*n + 1)]

    book = [[0]*n for _ in range(m)]

    out_directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    

    head = 0
    tail = 0

    book[x_init][y_init] = 1
    notes[tail].x = x_init
    notes[tail].y = y_init

    tail += 1
    
    max_score = count_scores(x_init, y_init, game_map)
    max_x = x_init
    max_y = y_init

    while head < tail:
        for out_direction in out_directions:
            tx = notes[head].x + out_direction[0]
            ty = notes[head].y + out_direction[1]

            if tx < 0 or tx >= m or ty < 0 or ty >= n:
                continue

            if book[tx][ty] == 0 and game_map[tx][ty] == ".":
                book[tx][ty] = 1
                notes[tail].x = tx
                notes[tail].y = ty
                tail += 1
                cur_scores = count_scores(tx, ty, game_map)
                if cur_scores > max_score:
                    max_score = cur_scores
                    max_x = tx
                    max_y = ty

        head += 1

    print(f"max_x: {max_x}")
    print(f"max_y: {max_y}")
    print(f"max_scores: {max_score}")

if __name__ == "__main__":
    main()