# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = ListNode(next=head)
        while head and head.next:
            head = head.next.next
            tail = tail.next
            if head == tail:
                return True
        return False