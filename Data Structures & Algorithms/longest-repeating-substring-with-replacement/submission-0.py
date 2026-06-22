class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0,0
        H = {}
        max_f = 0
        max_c = ""
        res = 0

        while r<len(s):

            H[s[r]] = H.get(s[r],0) + 1
            max_f = max(max_f,H[s[r]])

            if r-l+1 -max_f <= k:
                res = max(res,r-l+1)
            else:
                H[s[l]] = H[s[l]] - 1
                l = l + 1

            r = r+1


        return res







        