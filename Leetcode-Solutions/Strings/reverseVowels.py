class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=['a','e','i','o','u','A','E','I','O','U']
        l,r=0,len(s)-1
        s=[i for i in s]
        while l<r:
            while l<r and s[l] not in vowels:
                l+=1
            while r>l and s[r] not in vowels:
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)
        
        
