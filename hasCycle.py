# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

# lazy linkedlist declaration
class ListNode:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(self, head: ListNode) -> bool:
    # if empty linked list, return false
    if not head:
        return False

    slow = fast = head

    # if it is circle, then fast will catch up to slow at some point,
    # in which case would return true!
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
