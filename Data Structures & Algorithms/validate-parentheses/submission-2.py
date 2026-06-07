class Solution:
    def isValid(self, s: str) -> bool:

        observe = []
        pairs = {')':'(','}':'{',']':'['}

        for i in s:

            if i=='(' or i=='{' or i=='[':
                observe.append(i)

            else:

                if len(observe)==0:
                    return False

                temp = observe[-1]
                
                if temp!=pairs[i]:
                    return False
                
                observe.pop()

        if len(observe)==0:
            return True
        else:
            return False

            


        