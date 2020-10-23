# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# o(n)时间复杂度 o(1)空间复杂度
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # 快慢指针算中点
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_part_head = slow.next
        
        # 反转第二部分链表
        reverse_head = None
        while second_part_head:
            temp = second_part_head.next
            second_part_head.next = reverse_head
            reverse_head = second_part_head
            second_part_head = temp
        
        # 从头遍历原链表和反转链表,  前半的长度大于或等于后半, 当后半遍历完了如无出现错误, 则为回文链表
        while reverse_head:
            if head.val != reverse_head.val:
                return False
            head = head.next
            reverse_head = reverse_head.next
        
        return True
            
