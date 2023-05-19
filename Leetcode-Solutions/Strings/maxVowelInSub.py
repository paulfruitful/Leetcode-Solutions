class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength=float('-inf')
        currentLength=0
        right=0
        vowels=['A','E','I','O','U','a','e','i','o','u']

        for left in range(len(s)):
            if s[left] in vowels:
                currentLength+=1
            if k==left-right+1:
                if maxLength<currentLength:
                    maxLength=currentLength
                if s[right] in vowels:
                 currentLength-=1
                right+=1
        return maxLength
