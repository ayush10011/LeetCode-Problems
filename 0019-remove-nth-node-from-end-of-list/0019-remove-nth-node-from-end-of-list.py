# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = head

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Remove the head node
        if not fast:
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head