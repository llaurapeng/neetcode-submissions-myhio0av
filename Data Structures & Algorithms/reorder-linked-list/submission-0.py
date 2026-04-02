class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Find the middle of the list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second = slow.next
        slow.next = None  # End of the first half

        # Reverse the second half
        prev = None
        while second:
            after = second.next
            second.next = prev
            prev = second
            second = after

        # Now merge the two halves
        first, second = head, prev
        while second:
            # Save next nodes for both first and second parts
            firstnext, secondnext = first.next, second.next
            
            # Rearrange pointers
            first.next = second
            second.next = firstnext
            
            # Move to the next nodes in each half
            first = firstnext
            second = secondnext


        
        