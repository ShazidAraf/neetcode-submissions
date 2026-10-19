class TrieNode:

    def __init__(self):
        self.children = {}
        self.finish = False

    def addword(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.finish = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addword(word)

        m, n = len(board), len(board[0])
        res = set()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col, parent, word, visit):
            if row<0 or col<0 or row>m-1 or col>n-1 or (board[row][col] not in parent.children) or ((row,col) in visit):
                return

            ch = board[row][col]
            visit.add((row,col))
            node = parent.children[ch]
            word = word + ch
            if node.finish:
                res.add(word)
                node.finish = False                     # NEW: found once, stop counting it

            for dr, dc in dirs:
                dfs(row+dr, col+dc, node, word, visit)
            visit.remove((row,col))

            if not node.children and not node.finish:   # NEW: nothing left below this node
                del parent.children[ch]                 # cut the dead branch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "", set())

        return list(res)