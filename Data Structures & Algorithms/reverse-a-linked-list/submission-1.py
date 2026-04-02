# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while (curr): 
            #need to get curr to move to previous and set up to make the curr the next node
            afterCurr = curr.next 
            curr.next = prev
            prev = curr

            curr = afterCurr

        return prev

            
        