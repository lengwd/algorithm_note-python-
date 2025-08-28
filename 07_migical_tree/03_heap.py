from typing import Tuple

def swap(x: int, y: int, h: list) -> None:
    h[y], h[x] = h[x], h[y]

def siftDown(i: int, h: list, heap_size: int) -> None:

    

    while True:
        left = 2 * i
        right = 2 * i + 1
        min_idx = i

        if left <= heap_size and h[min_idx] > h[left]:
            min_idx = left
        if right <= heap_size and h[min_idx] > h[right]:
            min_idx = right

        if min_idx != i:
            swap(i, min_idx, h)
            i = min_idx
        else:
            break 

def create(h: list) -> None:
    heap_size =  len(h) - 1
    for i in range(heap_size//2, 0, -1):
        siftDown(i, h, heap_size)


def deleteMin(h: list, n: int) -> Tuple[list, int, int]:
    t = h[1]
    h[1] = h[n]
    n -= 1
    siftDown(1, h, n)

    return h, n, t


def main():
    h = [-1]
    nums = int(input("nums: "))
    # for i in range(nums):
    #     data = int(input(f"input data{i+1}: "))
    #     h.append(data)
    data_str = input("input data: ").split()
    data = [int(x) for x in data_str]

    h.extend(data)

    create(h)

    n = nums
    for _ in range(nums):
        h, n, t = deleteMin(h, n)
     
        print(t, end=" ")

if __name__ == "__main__":
    main()
    