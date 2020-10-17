# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        node = head
        while node:
            l.append(node)
            node = node.next
            
        res_head = ListNode()
        cur = res_head
        i, j = 0, len(l) - 1
        while i < j:
            cur.next = l[i]
            cur = cur.next
            cur.next = l[j]
            cur = cur.next
            i += 1
            j -= 1
        
        if i == j:
            cur.next = l[i]
            cur = cur.next
        
        cur.next = None
            
        return res_head.next
