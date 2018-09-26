#Remove Dups: Write code to remove duplicates from an unsorted linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        return

    def display(self):
        tempvar = self.head
        while tempvar:
            print (tempvar.data, '->', end=' ')
            tempvar = tempvar.next
            pass
        print ('')
        return

    def removeDuplicates(self):
        if self.head is None or self.head.next is None:
            return

        currPtr = self.head
        while currPtr:
            nextPtr = currPtr.next
            prevPtr = currPtr
            while nextPtr:
                if currPtr.data == nextPtr.data:
                    prevPtr.next = nextPtr.next
                else:
                    prevPtr = nextPtr
                nextPtr = nextPtr.next
            currPtr = currPtr.next
        return


def main():
    head = LinkedList()
    head.push(3)
    head.push(3)
    # head.push(2)
    head.display()
    # head.push(3)

    head.display()
    head.removeDuplicates()
    print ('after duplicates')
    head.display()

if __name__ == '__main__':
    main()

