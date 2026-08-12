# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def same_tree(p,q):
    if p is None and q is None:
        return True

    if (p is None and q is not None) or (p is not None and q is None) or p.val!=q.val:
        return False

    return same_tree(p.left,q.left) and same_tree(p.right,q.right)

class Solution:   
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True          # empty tree is a subtree of anything
        if root is None:
            return False         # non-empty subRoot can't fit in empty tree

        return (same_tree(root, subRoot)
                or self.isSubtree(root.left,  subRoot)
                or self.isSubtree(root.right, subRoot))




            
        