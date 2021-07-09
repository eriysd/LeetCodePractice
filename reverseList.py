# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

class ListNode:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# tranversing each element while reassigning its next to the previous


def reverseList(head: ListNode) -> ListNode:
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

# recursion version with the same operation


def reverseList2(self, head):
    return self._reverse(head)


def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)


'''
failed brutal force
def reverseList(head: ListNode) -> ListNode:
    if head:
        length = 1
    else:
        return head

    left = right = head

    while right.next:
        right = right.next
        length += 1

    for times in range(length//2):
        left.val, right.val = right.val, left.val
        left = left.next
        right = left
        for _ in range(length - 2*times - 1):
            right = right.next

    return head
'''


myList = ListNode()
myList.head = Node(3)
myList.head.next = Node(1)
myList.head.next.next = Node(3)
myList.head.next.next.next = Node(4)
myList.head.next.next.next.next = Node(1)
myList.head.next.next.next.next.next = Node(4)
myList.head.next.next.next.next.next.next = Node(-1)

print(reverseList(myList.head))
