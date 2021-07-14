# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/discuss/9771/Simple-5-lines-Python

# lazy linkedlist declaration
class ListNode:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# straight forward method


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = temp = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next

    temp.next = l1 or l2

    return dummy.next


# from discussion recursion method
def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2


def mergeTwoLists2(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a
