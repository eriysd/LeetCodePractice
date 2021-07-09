# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if fast == None:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


myList = LinkedList()
myList.head = Node(1)
myList.head.next = Node(2)
myList.head.next.next = Node(3)
myList.head.next.next.next = Node(4)
myList.head.next.next.next.next = Node(5)

print(removeNthFromEnd(myList.head, 2))
