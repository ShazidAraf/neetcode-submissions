class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(9):
            # print(i)

            row = board[i]
            col = [board[j][i] for j in range(9)]
            
            br = i // 3       
            bc = i % 3       
            box_rows = board[3*br : 3*br + 3]

            box = []

            for r in range(3):
                box += box_rows[r][3*bc : 3*bc + 3]




            # box = [box_rows[r][3*bc + c] for r in range(3) for c in range(3)]

            # print(box)

            x = self.check_repeat(row)
            y = self.check_repeat(col)
            z = self.check_repeat(box)

            s = x*y*z

            if s==0:
                return False

        return True


    def check_repeat(self,S):

        H = {}

        for i in S:
            if i == "." :
                continue

            H[i] = H.get(i,0)+1

            if H[i]>1:
                return False

        return True
