# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        res = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('%')
        return ','.join(res)                 # separator

    def deserialize(self, data):
        vals = data.split(',')
        if vals[0] == '%':
            return None                      # not TreeNode
        root = TreeNode(int(vals[0]))
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()               # next real parent
            if vals[i] != '%':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != '%':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root


    # # Encodes a tree to a single string.
    # def serialize(self, root: Optional[TreeNode]) -> str:


    #     res = []

    #     q = collections.deque([root])


    #     while q:

    #         for _ in range(len(q)):
    #             node = q.popleft()

    #             if node:
    #                 res.append(str(node.val))

    #                 q.append(node.left)
    #                 q.append(node.right)

    #             else:
    #                 res.append('%')

    #     res = ''.join(res)
    #     # print(res)

    #     return res 


    # # Decodes your encoded data to tree.
    # def deserialize(self, data: str) -> Optional[TreeNode]:


    #     if len(data)==0:
    #         return TreeNode


    #     i = 1
    #     n = 2
    #     nodes = [TreeNode(val=int(data[0]))]

    #     while i<len(data):


    #         for _ in range(n):

    #             if data[i]=='%':
    #                 nodes.append(0)
    #             else:

    #                 p = TreeNode(val=int(data[i]))
    #                 nodes.append(p)

    #                 if i>0:                    
    #                     if i%2==0:
    #                         par_id = (i-2)//2
    #                         nodes[par_id].right = p
    #                     else:
    #                         par_id = (i-1)//2
    #                         nodes[par_id].left = p

    #             i+=1

    #         n = 2*n

    #     return nodes[0]












