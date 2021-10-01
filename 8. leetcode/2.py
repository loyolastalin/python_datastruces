# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()
        
        cur = head
        
        carry = 0
        
        while l1 or l2 or carry:
            
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
                
            if l2:
                sum += l2.val
                l2 = l2.next
            
            if sum >= 10:
                sum -= 10
                carry = 1
                
            else:
                carry = 0
                
                
            cur.next = ListNode(sum)
            
            cur = cur.next
            
        return head.next