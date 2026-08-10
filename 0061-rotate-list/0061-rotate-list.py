# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Avoid unnecessary rotations
        k %= length
        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # Find the new tail
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Node after new tail is the new head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head