/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var flag = true;
    var l3 = new ListNode(l1.val + l2.val);
    var l4 = l3;
    while (flag) {
        if (l1.next === null) {
            l4.next = l2.next;
            break;
        }else if (l2.next === null) {
            l4.next = l1.next;
            break;
        }else{
            l1 = l1.next;
            l2 = l2.next;
            l4.next = new ListNode(l1.val + l2.val);
            l4 = l4.next;
        }
        
    }
    
    l4 = l3;
    var temp = 0;
    while (l4 !== null) {
        l4.val = l4.val + temp;
        temp = l4.val >= 10 ? 1 : 0;
        l4.val = l4.val % 10;
        if (l4.next === null && temp === 1) {
            l4.next = new ListNode(1);
            temp = 0;
        }
        l4 = l4.next;
    }

    
    return l3;
};