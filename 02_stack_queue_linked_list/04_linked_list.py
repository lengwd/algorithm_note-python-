class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_end(head: LinkedList, num: int) -> LinkedList:
    inNode = LinkedList(num)

    if head is None: 

        return inNode
    
    cur = head
    while cur.next != None:
        cur = cur.next
    
    cur.next = inNode

    return head

def insert_mid(head: LinkedList, num: int) -> LinkedList:
    inNode = LinkedList(num)

    if head is None:
        return inNode
    
    cur = head
    while cur.next.value < num and cur.next !=None:
        cur = cur.next

    temp = cur.next
    cur.next = inNode
    cur = cur.next
    cur.next = temp

    return head

def main():
    data_s = input().split()
    data = [int(x) for x in data_s]

    head = None

    for d in data:
        head = insert_end(head, d)
    
    in_data =  int(input())

    head = insert_mid(head, in_data)



    cur =  head
    while cur.next != None:
        print(cur.value, end=" ")
        cur = cur.next
    print(cur.value, end=" ")

if __name__ == "__main__":
    main()