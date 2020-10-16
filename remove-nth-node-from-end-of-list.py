# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre, target, _next = None, None, None
        
        cur = head
        for _ in range(n):
            cur = cur.next
            
        target = head
        while cur:
            pre = target
            target = target.next
            cur = cur.next
        
        if pre:
            pre.next = target.next
            return head
        else:
            return head.next
