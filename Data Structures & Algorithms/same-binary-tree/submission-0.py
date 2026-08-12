# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        def dfs(x,y):


            if (x is None and y is None):
                return 1
            elif (x is None and y is not None) or (x is not None and y is None) or x.val!=y.val:
                return 0

            return dfs(x.left,y.left)*dfs(x.right,y.right)

        if dfs(p,q)==1:
            return True
        else:
            return False
        