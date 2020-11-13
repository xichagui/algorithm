# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        slow = fast = head
        while fast.next and fast.next.next:
            pre_slow = slow
            slow = slow.next
            pre_fast = fast.next
            fast = pre_fast.next
            
            pre_slow.next = fast
            pre_fast.next = fast.next
            fast.next = slow
            
            slow = fast
            fast = pre_fast
        
        return head

