# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if not head:
            return None
        
        _head1 = cur1 = ListNode(0)
        _head2 = cur2 = ListNode(0)
        
        cur = head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        
        if cur1 != _head1:
            cur2.next = None
            cur1.next = _head2.next
            
            return _head1.next
        else:
            return _head2.next
            
