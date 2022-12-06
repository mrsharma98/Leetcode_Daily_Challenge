class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head or not head.next or not head.next.next):
            return head
            
        odd, oddHEad, even, evenHead = None, None, None, None
        odd = head
        oddHead = odd
        even = head.next
        evenHead = even

        while (even and even.next):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = evenHead
        return oddHead
