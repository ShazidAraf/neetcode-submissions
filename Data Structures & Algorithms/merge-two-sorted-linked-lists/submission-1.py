# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        head = dummy


        while list1 and list2:


            if list1.val>=list2.val:

                dummy.next = list2
                list2 = list2.next

            else:

                dummy.next = list1
                list1 = list1.next

            dummy = dummy.next

        
        if (list1 is None) and (list2 is None):
            return head.next

        elif list1 is None:
            dummy.next = list2
            return head.next

        elif list2 is None:
            dummy.next = list1
            return head.next
        










        