class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        
        # dummy->1
        
        cur = dummy
        while cur and n >= 0:
            cur = cur.next
            n -= 1
            
        head = dummy    
            
        while cur:
            cur = cur.next
            head = head.next
            
        if head.next: head.next = head.next.next
        
        return dummy.next