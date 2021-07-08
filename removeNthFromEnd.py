# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


head = ListNode()
head.next = ListNode(1)


print(removeNthFromEnd(, 2))
