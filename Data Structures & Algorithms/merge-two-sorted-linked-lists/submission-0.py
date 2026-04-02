class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()  # Dummy node to hold the result
        end = ret  # Pointer to the last node in the merged list
        
        while list1 and list2:  # Iterate until one of the lists is exhausted

            if list1.val < list2.val:
                end.next = list1  # Attach list1's node
                list1 = list1.next  # Move to the next node in list1
                end = end.next  # Move end to the newly added node
            else:
                end.next = list2  # Attach list2's node
                list2 = list2.next  # Move to the next node in list2
                end = end.next  # Move end to the newly added node

        # If either list1 or list2 is not exhausted, append the remaining nodes
        if list1:
            end.next = list1
        if list2:
            end.next = list2
        
        return ret.next  # Return the merged list starting from the node after the dummy node
