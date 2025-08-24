nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] # 用于数字对应火柴棍数量

# a + b = c
def count_matchstick(number: int) -> int:
    if number == 0:
        return nums[0]
    sum = 0
    while(number>0):
        ge = number % 10
        sum += nums[ge]
        number //= 10
    return sum


def a_plus_b_equal_c(m): # m 是输入的火柴棍的数量
    total = 0
    for a in range(1112):
        for b in range(1112):
            sum_a = count_matchstick(a)
            sum_b = count_matchstick(b)
            sum_c = count_matchstick(a+b)
            if sum_a + sum_b + sum_c == m - 4:
                total += 1
                print(f"{a}+{b}={a+b}")

def main():
    m = int(input("输入火柴棍的数量："))
    a_plus_b_equal_c(m)

if __name__ == "__main__":
    main()