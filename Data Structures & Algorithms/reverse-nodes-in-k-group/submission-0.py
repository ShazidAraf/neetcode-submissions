# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        answer_head = head
        prev_tail = None
        curr_head = head

        while curr_head:
            flag, next_l = self.length_checker(curr_head, k)
            if not flag:
                break                     

            rev_head = self.reverse(curr_head) 
            if prev_tail is None:
                answer_head = rev_head
            else:
                prev_tail.next = rev_head  

            curr_head.next = next_l
            prev_tail = curr_head
            curr_head = next_l

        return answer_head



    def reverse(self,h):

        prev = None
        curr = h

        while curr:

            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp
        
        return prev

    
    def length_checker(self,h,k):


        curr = h
        n = 0
        while curr:
            n+=1

            if n==k:
                break

            curr = curr.next

        if n==k:
            flag = 1
            fut = curr.next
            curr.next = None
            return flag,fut
        else:
            flag = 0
            return 0,None




