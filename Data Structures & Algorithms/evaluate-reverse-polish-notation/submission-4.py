import numpy as np

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        self.stack = []


        for i in range(len(tokens)):


            if tokens[i] not in '+-*/':
                self.stack.append(int(tokens[i]))
            else:
                a = self.stack.pop()
                b = self.stack.pop()
                
                if tokens[i]=="+":
                    self.stack.append(a+b)

                if tokens[i]=="-":
                    self.stack.append(b-a)

                if tokens[i]=="*":
                    self.stack.append(b*a)

                if tokens[i]=="/":

                    tmp = b/a

                    if tmp>=0:
                        k = int(np.floor(tmp))
                    
                    else:
                        k = int(np.ceil(tmp))

                    self.stack.append(k)
        
            print(self.stack)

        return self.stack[0]


                    


        
