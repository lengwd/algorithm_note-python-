def main():
    m = int(input("people nums: "))
    n = int(input("hints: "))

    h = [-1]
    peoples = [x for x in range(1, m+1)]
    h.extend(peoples)




    def getBoss(v: int, h: list) -> int:
        if h[v] == v:
            return v
        
        else:
            h[v] = getBoss(h[v], h)
            return h[v]
        
    def merge(left: int, right: int, h: list):
        t1 = getBoss(left, h)
        t2 = getBoss(right, h)

        if t1 != t2:
            h[t2] = t1


    for _ in range(n):
        data_in = [int(x) for x in input("input hint: ").split()]
        left =  data_in[0]
        right = data_in[1]

        merge(left, right, h)

    total = 0
    for i in range(1, m+1):
        if h[i] == i:
            total += 1

    print(f"total: {total}")


if __name__ == "__main__":
    main()