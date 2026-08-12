# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        self.res = 0



        def dfs(curr):

            if curr is None:
                return 0

            left_h = dfs(curr.left)
            right_h = dfs(curr.right)


            d = abs(left_h-right_h)
            self.res = max(self.res,d)

            return 1+max(left_h,right_h)


        dfs(root)

        if self.res>1:
            return False
        else:
            return True




        