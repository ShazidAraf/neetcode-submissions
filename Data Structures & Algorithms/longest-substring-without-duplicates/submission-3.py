class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        max_len = 0
        H = {}

        while r<len(s):


            if s[r] in H:
                
                tmp = H[s[r]]+1
                for i in range(l,H[s[r]]):
                    H.pop(s[i])
                
                l = tmp

            
            H[s[r]] = r
            max_len = max(max_len,(r-l+1))

            print(s[l:r+1])
            print(H)

            r+=1



        return max_len




        
        