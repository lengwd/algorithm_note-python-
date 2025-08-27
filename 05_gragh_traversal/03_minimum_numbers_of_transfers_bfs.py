
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
        # c = int(input("distance: "))
        arr[a][b] = 1
        arr[b][a] = 1
        print()

    return arr

class Notes:
    def __init__(self):
        self.x = None
        self.s = None

def main():

    start = int(input("input start city: ")) - 1
    end = int(input("input end city: ")) - 1

    flag = False

    arr = read_map()
    w = len(arr)
    book = [0] * w

    notes = [Notes() for _ in range(w+1)]

    # initial
    head = 0
    tail = 0

    book[start] = 1
    notes[tail].x = start
    notes[tail].s = 0
    tail += 1

    while head < tail:
        for i in range(w):
            if book[i] == 0 and arr[head][i] != float("inf"):
                book[i] = 1
                notes[tail].x = i
                notes[tail].s = notes[head].s + 1
                tail += 1

                if i == end:
                    flag = True
                    print(notes[tail-1].s)
        
        if flag == True:
            break

        head += 1


if __name__ == "__main__":
    main()    
    