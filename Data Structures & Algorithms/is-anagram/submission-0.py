class Solution(object):

    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if self.create_keys(s)==self.create_keys(t):
            return True
        else:
            return False
            
    def create_keys(self,s):

        H = [0]*26

        for s1 in s:
            H[ord(s1)-ord('a')]+=1
        
        return tuple(H)
        