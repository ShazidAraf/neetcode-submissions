class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:



        A = nums1
        B = nums2

        if len(A) < len(B):
            A,B = B,A

        l,r = 0, len(B)-1
        
        total_len = len(A) + len(B)

        while(1):

            m = (l+r)//2
            k = total_len // 2 - m - 2     # was: total_len // 2 - m

            B_left = B[m] if m >= 0 else float('-inf')
            B_right = B[m+1] if m+1 < len(B) else float('inf')

            A_left = A[k] if k >= 0 else float('-inf')
            A_right = A[k+1] if k+1 < len(A) else float('inf')

            if B_left<=A_right and A_left<=B_right:

                if total_len % 2:
                    return min(A_right,B_right)
                else:
                    return (max(A_left,B_left) + min(A_right,B_right))/2


            elif B_left>A_right:
                r = m-1
            elif A_left>B_right:
                l = m+1


        
        