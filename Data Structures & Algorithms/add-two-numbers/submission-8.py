# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the result linked list and a pointer (nums) to keep track of the current node.
        dummy_head = ListNode(0)  # This will point to the head of the result list.
        current = dummy_head  # Pointer to construct the list.
        carry = 0  # Initialize carry over.

        # Traverse both linked lists until both are exhausted.
        while l1 or l2:
            # Get the values from l1 and l2, if they exist, otherwise 0.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the two digits and the carry.
            total_sum = val1 + val2 + carry
            carry = total_sum // 10  # Calculate the new carry for the next iteration.
            current_digit = total_sum % 10  # Get the digit to store in the result.

            # Create a new node for the current digit and move the pointer.
            current.next = ListNode(current_digit)
            current = current.next

            # Move to the next nodes in l1 and l2 if they exist.
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # If there is a carry left after processing both lists, add it as a new node.
        if carry:
            current.next = ListNode(carry)

        # Return the head of the result list (skipping the dummy head).
        return dummy_head.next
