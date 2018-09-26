#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

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

    def displayLL(self):
        tempPtr = self.head
        while tempPtr:
            print (tempPtr.data,' -> ',end= ' ')
            tempPtr = tempPtr.next
            pass
        print ('')
        return

    def getLastKthElement(self,K):
        count = 0
        currPtr,prevPtr = self.head,self.head
        while currPtr and count < K:
            count += 1
            currPtr = currPtr.next
        while currPtr:
            currPtr = currPtr.next
            prevPtr = prevPtr.next
        return (prevPtr.data)



def main():
    head = SinglyLinkedList()
    print("Execution started:")
    head.pushAtStart(2)
    head.pushAtStart(22)
    head.pushAtStart(32)
    head.pushAtStart(52)
    head.pushAtStart(62)
    head.displayLL()
    lastK = head.getLastKthElement(232)
    print ('lastKth element is: ',lastK)
    return


if __name__ == '__main__':
    main()