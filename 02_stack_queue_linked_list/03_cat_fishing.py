from typing import *

### 我这是现实版的小猫钓鱼
###C代码的匹配规则：

# 只检查栈顶的一张牌是否与出的牌相同
# 如果栈顶匹配，只取走栈顶这一张牌
# 这是简化版的"小猫钓鱼"规则
# 你的Python代码匹配规则：

# 检查整个栈中是否有匹配的牌
# 如果找到匹配，取走从匹配位置到栈顶的所有牌
# 这是完整版的"小猫钓鱼"规则


class Queue:
    def __init__(self):
        self.data = [0 for _ in range(100)]
        self.head = 0
        self.tail = 0


class Stack:
    def __init__(self):
        self.data = [0 for _ in range(10)]
        self.top = -1


def compare_stack(num: int, stack: Stack) -> List:
    original_top = stack.top
    for i in range(stack.top, -1, -1):
        if num == stack.data[i]:
            stack.top = i - 1
            return stack.data[i:original_top+1][::-1]
    return None
        



def main():
    q1 = Queue()
    q2 = Queue()
    s = Stack()



    data1_s = input().split()
    data1 = [int(x) for x in data1_s]
    len_data1 = len(data1)
    q1.data[0:len_data1] = data1
    q1.tail = len_data1

    data2_s = input().split()
    data2 = [int(x) for x in data2_s]
    len_data2 = len(data2)
    q2.data[0:len_data2] = data2
    q2.tail = len_data2

   

    while (q1.head<q1.tail) and (q2.head < q2.tail):
        # 1 号出牌
        q1_out = q1.data[q1.head]
        q1.head += 1

        # 判断栈对立面有没有对应的数
        re1 = compare_stack(q1_out, s)

        if re1:
            # q1队列加牌
            q1.data[q1.tail] = q1_out
            q1.tail += 1
            for i in range(len(re1)):
                
                q1.data[q1.tail] = re1[i]
                q1.tail += 1
            # 栈减牌已经在在函数中实现了
        else:
            # 牌堆加牌
            s.top += 1
            s.data[s.top] = q1_out
        if q1.head == q1.tail:
            break

        # 2号出牌
        q2_out = q2.data[q2.head]
        q2.head += 1

        # 判断栈对立面有没有对应的数
        re2 = compare_stack(q2_out, s)

        if re2:
            q2.data[q2.tail] = q2_out
            q2.tail += 1
            for i in range(len(re2)):
                q2.data[q2.tail] = re2[i]
                q2.tail += 1
                # 栈减牌已经在在函数中实现了
        else:
            s.top += 1
            s.data[s.top] = q2_out

    if q1.head == q1.tail:
        print("小哈win")
        print("手上的牌为：", end="")
        for i in q2.data[q2.head: q2.tail]:
            print(i, end=" ")
        print()
        print("桌上的牌：", end="")
        for i in s.data[:s.top+1]:
            print(i, end=" ")
    elif q2.head == q2.tail:
        print("小哼win")
        print("手上的牌为：", end="")
        for i in q1.data[q1.head: q1.tail]:
            print(i, end=" ")
        print()
        print("桌上的牌：", end="")
        for i in s.data[:s.top+1]:
            print(i, end=" ")
    else:
        print("something wrong")

if __name__ == "__main__":
    main()








