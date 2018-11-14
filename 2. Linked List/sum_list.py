class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def display(self):
        A = self.head
        while A:
            print (A.data, end= "--")
            A  = A.next

def add_two_list(A,B):
    print (type(A))
    if A is None:   return B
    if B is None:   return A
    carry = 0
    #A.display()
    print ("")
    #B.display()
    while A or B:
        if A is not None:
            x = A.data
        else:
            x = 0
        y = B.data if B is not None else 0
        if A: A = A.next
        if B: B = B.next
        print (x+y)
    pass

def main():
    head = LinkedList()
    head.insert(2)
    head.insert(3)
    head.insert(4)
    head.insert(5)
    head.display()
    head2 = LinkedList()
    head2.insert(2)
    head2.insert(3)
    head2.insert(4)
    head2.insert(5)
    head2.display()
    add_two_list(head.head,head2.head)
if __name__ == "__main__":
    main()
