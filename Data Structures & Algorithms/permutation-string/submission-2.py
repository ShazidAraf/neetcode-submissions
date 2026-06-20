class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        # Make Sliding window s2
        # for each sliding window on s2, check whether it is a permutation of s1
        
        if len(s2)<len(s1):
            return False
            
        Counr_s1 = [0]*26
        Counr_s2 = [0]*26


        for i in range(len(s1)):
            Counr_s1[ord(s1[i]) - ord('a')]+=1

        for i in range(len(s1)):
            Counr_s2[ord(s2[i]) - ord('a')]+=1

        match = 0

        for i in range(26):
            if Counr_s1[i]==Counr_s2[i]:
                match+=1



        l = 0
        r = len(s1) - 1


        while r< len(s2)-1:

            if match==26:
                return True

            # Counr_s2[ord(s2[r]) - ord('a')]+=1
            r = r+1
            Counr_s2[ord(s2[r]) - ord('a')]+=1

            if Counr_s2[ord(s2[r]) - ord('a')] == Counr_s1[ord(s2[r]) - ord('a')] +1:
                match = match-1
            elif Counr_s2[ord(s2[r]) - ord('a')] == Counr_s1[ord(s2[r]) - ord('a')]:
                match = match+1
            

            
            Counr_s2[ord(s2[l]) - ord('a')]-=1
            if Counr_s2[ord(s2[l]) - ord('a')] == Counr_s1[ord(s2[l]) - ord('a')] -1:
                match = match-1
            elif Counr_s2[ord(s2[l]) - ord('a')] == Counr_s1[ord(s2[l]) - ord('a')]:
                match = match+1

            l = l+1

        if match==26:
            return True
        else:
            return False













