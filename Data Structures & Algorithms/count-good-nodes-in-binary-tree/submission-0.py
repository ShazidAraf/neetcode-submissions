# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.result = 0



        def dfs(curr,curr_max):


            if curr is None:
                return

            if curr.val>=curr_max:
                self.result += 1

            curr_max = max(curr_max,curr.val)


            left = dfs(curr.left, curr_max)
            right = dfs(curr.right, curr_max)


            return


        dfs(root,-100)

        return self.result









        