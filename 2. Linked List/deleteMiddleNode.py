# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f

import ListOperations as listopr



def deleteMiddle(head):
    if head is None or head.next is None:
        head = None
        return
    else:
        slowptr,fastptr = head,head
        while fastptr and fastptr.next and fastptr.next.next:
            slowptr = slowptr.next
            fastptr = fastptr.next
            if fastptr.next:
                fastptr.next = fastptr.next
        slowptr.next = slowptr.next.next
    return


def main():
    head = listopr.LinkedList()
    head.push(5)
    #head.push(9)
    #head.push(99)
    head.display()
    head.deleteMiddle()
    #deleteMiddle(head)
    head.display()



if __name__ == "__main__":
    main()