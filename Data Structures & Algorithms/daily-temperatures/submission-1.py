class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        result = [0]*len(temperatures)
        stack = []



        for i in range(len(temperatures)):

            if i==0:
                stack.append([temperatures[i],i])

            while(stack):
                if temperatures[i]>stack[-1][0]:
                    temp,idx = stack.pop()
                    result[idx] = i-idx
                    
                else:
                    break

            stack.append([temperatures[i],i])

        return result

            


        