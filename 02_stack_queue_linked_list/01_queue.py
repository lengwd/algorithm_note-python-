## 解密QQ号其实用python实现很简单 因为python又append和pop 
## 但是为了学习指针等算法的精髓 还是用指针来实现
## 做一个工程应该 KISS 但是学习的时候可以稍微 探索一下

class Queue:
    def __init__(self):
        self.data = [0 for _ in range(100)]
        self.head = None
        self.tail = None

def main():
    data_in = input().split()
    data_int = [int(x) for x in data_in]
    l = len(data_in)

    q = Queue()
    q.data[:l] = data_int
    q.head = 0
    q.tail = l

    
    while q.head < q.tail:
        ## 删除第一个
        print(q.data[q.head], end=" ")
        q.head += 1

        ## 移动第二个
        q.data[q.tail] = q.data[q.head]
        q.head += 1
        q.tail += 1
    

if __name__ == "__main__":
    main()