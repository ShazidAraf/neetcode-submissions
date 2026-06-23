from collections import Counter 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        

        if len(s)<len(t):
            return ""

        # Create Hashmap of t
        T = Counter(t)

        # Create Hashmap of s[0:len(t)]
        S = Counter(s[0:len(t)])

        # Calculate Match
        match = 0
        for key in T:
            if key in S:
                if S[key] >= T[key]:
                    match+=1


        # Create Loop
        # left pointer - l
        # Right pointer - r
        # Keep on inclearing right pointer until match==len(T)
        
        l,r = 0,len(t)-1
        min_len = float('inf')
        result = ""

        while r<len(s):

            while match==len(T):

                if r-l+1 < min_len:
                    result = s[l:r+1]
                    min_len = r-l+1


                if s[l] in T:
                    if S[s[l]] == T[s[l]]:
                        match -= 1
                S[s[l]]-=1
                l = l+1


            r = r+1

            if r>len(s)-1:
                continue

            S[s[r]] = S.get(s[r],0)+1
            if s[r] in T:             
                if S[s[r]]==T[s[r]]:
                    match+=1

        
        return result








