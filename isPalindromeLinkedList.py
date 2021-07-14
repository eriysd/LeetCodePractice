# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

# lazy linkedlist declaration
class ListNode:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# traditional approach


def isPalindrome(self, head: ListNode) -> bool:

    # find the centre
    slow = fast = head
    while fast and fast.next:  # as long as there is next
        fast = fast.next.next
        slow = slow.next

    # reverse the second half
    node = None
    while slow:
        slow.next, node, slow = node, slow, slow.next

    # compare the halves
    while node:
        if head.val != node.val:
            return False
        head = head.next
        node = node.next
    return True

# fast approach


def isPalindrome1(self, head: ListNode) -> bool:
    myList = list()

    while head:
        myList.append(head.val)
        head = head.next

    return myList == myList[::-1]
