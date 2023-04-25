class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1,len2=len(word1),len(word2)
        merged=''
        maxSize=max(len1,len2)

        for i in range(maxSize):
            if i<len1:
                merged+=word1[i]
            if i<len2:
                merged+=word2[i]
        return merged


