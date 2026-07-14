# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # Count Number of Nodes

        dummy = head

        count = 0
        while dummy:
            dummy = dummy.next
            count+=1

        print(count)
        # Reach the nth node from the alast
        m = count - n

        # Dummy2
        dummy2 = ListNode()
        dummy2.next = head


        # Remove it
        dummy = dummy2
        for i in range(m):
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return dummy2.next

        