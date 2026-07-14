# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:



        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        for i in range(len(lists) - 1):

            if i == 0:
                list1 = lists[0]
                list2 = lists[1]
            else:
                list1 = concat
                list2 = lists[i + 1]

            concat = self.merge_list(list1, list2)

        return concat

    def merge_list(self, list1, list2):

        dummy = ListNode()
        head = dummy

        while list1 or list2:

            l1 = list1.val if list1 else float('inf')
            l2 = list2.val if list2 else float('inf')

            if l1 <= l2:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        return head.next





        