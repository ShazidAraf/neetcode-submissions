# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Get Length of ListNode
        count = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            count+=1

        # print(count)

        # Break into 2 portions
        dummy = head
        for i in range((count + 1) // 2 - 1):
            dummy = dummy.next
        half = dummy.next
        dummy.next = None  

        # print(half)

        # Reverse one part
        prev = None
        curr = half

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        half_rev = prev

        # print(half_rev)

        # Concatenate
        dummy = ListNode()

        while half_rev:

            dummy.next = head
            head = head.next
            dummy = dummy.next
            
            dummy.next = half_rev
            half_rev = half_rev.next
            dummy = dummy.next

        if head:
            dummy.next = head






