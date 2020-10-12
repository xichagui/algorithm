# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        root = pre_head = ListNode()
        pre_head.next = head
        
        while head and head.next:
            next_node = head.next
            head.next = next_node.next
            next_node.next = head
            
            pre_head.next = next_node
            
            pre_head = head
            head = head.next
            
        return root.next
