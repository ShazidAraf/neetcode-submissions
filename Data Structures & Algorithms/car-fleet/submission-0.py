class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:



        # Make Pairs

        pairs = [[position[i],speed[i]] for i in range(len(speed))]
        stack = []

        # High to Low sorted
        for p,s in sorted(pairs)[::-1]: 

            t = (target-p)/s
            stack.append(t)

            if len(stack)>1:
                if stack[-2]>=stack[-1]:
                    stack.pop()

        return len(stack)



        