# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:




        Q = collections.deque([root])

        result = []


        while Q:

            level = []
            for i in range(len(Q)):

                node = Q.popleft()

                if node:
                    Q.append(node.left)
                    Q.append(node.right)
                    level.append(node.val)

            if len(level)>0:
                result.append(level)

        return result


        