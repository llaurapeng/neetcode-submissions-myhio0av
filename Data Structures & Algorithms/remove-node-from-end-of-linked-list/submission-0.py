# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length 

        dummylen = head
        leng = 0 

        while dummylen: 
            leng+=1
            dummylen = dummylen.next

        ridOf = leng - n

        if ridOf == 0: 
            return head.next

        counter = 0
        start = head
        ret = head

        while start:
            #keep track of the prev
            if counter == ridOf: 
                after = start.next
                prev.next = after
                break
            else: 
                prev = start
                start = start.next

            counter+=1

            
        return ret

        

        


        