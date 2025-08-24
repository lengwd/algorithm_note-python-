# test1: ()3 x 6528 = 3() x 8256
def test_1():
    sum =  0
    for x in range(1, 10, 1):
        left = (x * 10 + 3) * 6528
        right = (30 + x) * 8256

        if left == right:
            print(x)
            sum += 1

    print(f"总共有{sum}个解")

# ()()() + ()()() = ()()()
def test_2():
    sum = 0
    for a1 in range(1, 10, 1):
        for a2 in range(1, 10, 1):
            for a3 in range(1, 10, 1):
                for a4 in range(1, 10, 1):
                    for a5 in range(1, 10, 1):
                        for a6 in range(1, 10, 1):
                            for a7 in range(1, 10, 1):
                                for a8 in range(1, 10, 1):
                                    for a9 in range(1, 10, 1):
                                        if a1 not in [a2, a3, a4, a5, a6, a7, a8, a9]:
                                            if a2 not in [a3, a4, a5, a6, a7, a8, a9]:
                                                if a3 not in [a4, a5, a6, a7, a8, a9]:
                                                    if a4 not in [a5, a6, a7, a8, a9]:
                                                        if a5 not in [a6, a7, a8, a9]:
                                                            if a6 not in [a7, a8, a9]:
                                                                if a7 not in [a8, a9]:
                                                                    if a8 != a9:
                                                                        left1 = a1 * 100 + a2 * 10 + a3
                                                                        left2 = a4 * 100 + a5 * 10 + a6
                                                                        right = a7 * 100 + a8 * 10 + a9
                                                                        if left1 + left2 == right:
                                                                            print(f"{a1}{a2}{a3}+{a4}{a5}{a6}={a7}{a8}{a9}")
                                                                            sum += 1
    print(f"总共有{sum}个解")
                                                            

def test_2_improve():
    total = 0
    
    for a1 in range(1, 10, 1):
        for a2 in range(1, 10, 1):
            for a3 in range(1, 10, 1):
                for a4 in range(1, 10, 1):
                    for a5 in range(1, 10, 1):
                        for a6 in range(1, 10, 1):
                            for a7 in range(1, 10, 1):
                                for a8 in range(1, 10, 1):
                                    for a9 in range(1, 10, 1):
                                        book = [0 for _ in range(10)]
                                        sum1 = 0
                                        for a in [a1, a2, a3, a4, a5, a6, a7, a8, a9]:
                                            book[a] = 1
                                        sum1 = sum(book)
                                        if sum1 == 9:
                                            left1 = a1 * 100 + a2 * 10 + a3
                                            left2 = a4 * 100 + a5 * 10 + a6
                                            right = a7 * 100 + a8 * 10 + a9
                                            if left1 + left2 == right:
                                                print(f"{a1}{a2}{a3}+{a4}{a5}{a6}={a7}{a8}{a9}")
                                                total += 1
    print(f"总共有{total}个解")




if __name__ == "__main__":
    # test_1()
    # test_2()
    test_2_improve()