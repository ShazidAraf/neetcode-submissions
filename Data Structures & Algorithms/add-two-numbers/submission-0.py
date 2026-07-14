# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        head = dummy
        c = 0
        
        while (1):

            if l1:
                p = l1.val
            else:
                p = 0
            
            if l2:
                q = l2.val
            else:
                q = 0

            s = (p+q+c)%10
            c = (p+q+c)//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            dummy.val = s

            if l1 is None and  l2 is None:
                break

            dummy.next = ListNode()
            dummy = dummy.next

        
        if c==0:
            dummy.next= None
        else:
            dummy.next = ListNode(c)


        return head






            
        


            





