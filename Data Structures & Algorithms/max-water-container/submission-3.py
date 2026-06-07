class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        max_storange = 0


        l = 0
        r = len(heights) - 1


        while l<r:

            storage = min(heights[l],heights[r])*(r-l)
            max_storange = max(max_storange,storage)


            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return max_storange


