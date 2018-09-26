class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def pushAtStart(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pushAtEnd(self,data):
        tempnode =  self.head
        if not tempnode:
            self.head = Node(data)
        while tempnode and tempnode.next:
            tempnode = tempnode.next
        tempnode.next = Node(data)


    def displayLL(self):
        tempPtr = self.head
        while tempPtr:
            print (tempPtr.data,' -> ',end= ' ')
            tempPtr = tempPtr.next
            pass
        print ('')
        return



def main():
    head = SinglyLinkedList()

    print("Execution started:")
    head.pushAtStart(2)
    head.pushAtStart(22)

    head.displayLL()
    head.pushAtEnd(22322)
    head.displayLL()
    return


if __name__ == '__main__':
    main()