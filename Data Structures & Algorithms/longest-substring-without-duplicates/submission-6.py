class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        l = 0
        r = 0
        H = {}

        while r<len(s):

            H[s[r]] = H.get(s[r],0)+1

            if H[s[r]]>1:

                for i in range(l,r):

                    H.pop(s[l])
                    l+=1

                    if s[l-1]==s[r]:
                        H[s[r]] = 1
                        break


            max_len = max(max_len,r-l+1)
            r = r+1

        return max_len



        
        