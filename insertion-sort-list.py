# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        cur = head
        last = cur
        
        while cur.next:
            last = cur
            cur = cur.next
            
            pre = dummy_head
            temp = dummy_head.next
            
            
            while temp != cur:
                if cur.val < temp.val:
                    last.next = cur.next
                    pre.next = cur
                    cur.next = temp
                    cur = last
                    break
                pre = temp
                temp = temp.next
                
        return dummy_head.next

