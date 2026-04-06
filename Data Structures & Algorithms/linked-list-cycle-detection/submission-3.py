# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = ListNode(next=head)
        while head and tail:
            head = head.next
            for i in range(2):
                if head:
                    head = head.next
            tail = tail.next
            if head and tail and head.val <= tail.val:
                return True
        return False