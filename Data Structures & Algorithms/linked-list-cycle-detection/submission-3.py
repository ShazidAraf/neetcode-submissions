# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        fast, slow = head, head


        while (1):
            
            if slow and fast:
                slow = slow.next
                fast = fast.next
            else:
                return False

            if fast:
                fast = fast.next
            else:
                return False

            if fast:
                if slow==fast:
                    return True
            else:
                return False


        

