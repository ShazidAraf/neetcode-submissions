# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # if len(preorder)==0 or len(inorder)==0:
        #     return None

        # root = TreeNode(val = preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1],inorder[0:mid])
        # root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        # return root

        pos = {v: i for i, v in enumerate(inorder)}
        self.p = 0
        def build(lo, hi):
            if lo > hi:
                return None
            val = preorder[self.p]
            self.p += 1
            root = TreeNode(val)
            root.left = build(lo, pos[val] - 1)
            root.right = build(pos[val] + 1, hi)
            return root
        return build(0, len(inorder) - 1)
        