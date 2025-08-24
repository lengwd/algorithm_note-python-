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

def find_place_can_kill_most():
    sum_max = 0
    # tx_max = 0
    # ty_max = 0
    for i in range(13):
        for j in range(13):
            if game_map[i][j] != ".":
                continue
            tx = i
            ty = j
            sum_single = 0

            while True:
                if game_map[tx][ty] == "#":
                    break
                if game_map[tx][ty] == "G":
                    sum_single += 1
                tx += 1

            tx = i
            ty = j
            while True:
                if game_map[tx][ty] == "#":
                    break
                if game_map[tx][ty] == "G":
                    sum_single += 1
                ty += 1

            tx = i
            ty = j
            while True:
                if game_map[tx][ty] == "#":
                    break
                if game_map[tx][ty] == "G":
                    sum_single += 1
                tx -= 1

            tx = i
            ty = j
            while True:
                if game_map[tx][ty] == "#":
                    break
                if game_map[tx][ty] == "G":
                    sum_single += 1
                ty -= 1

            if sum_max < sum_single:
                sum_max = sum_single
                tx_max = i
                ty_max = j
    print(f"最大数量为{sum_max}, 坐标为({tx_max},{ty_max})")

if __name__ == "__main__":
    find_place_can_kill_most()


