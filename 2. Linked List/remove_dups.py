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

def main():
    head = LinkedList()
    head.push(2)
    head.push(3)
    head.push(3)
    head.display()
    head.push(2)

    head.display()


if __name__ == '__main__':
    main()

