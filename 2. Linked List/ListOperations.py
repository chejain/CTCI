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

    def deleteMiddle(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return
        else:
            prevptr = None
            slowptr, fastptr = self.head, self.head
            while fastptr and fastptr.next:
                prevptr = slowptr
                slowptr = slowptr.next
                fastptr = fastptr.next
                if fastptr.next:
                    fastptr = fastptr.next
            if slowptr:
                print (slowptr.data, prevptr.data)
                prevptr.next = prevptr.next.next
        return