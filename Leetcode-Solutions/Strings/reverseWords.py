class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        s=[i[::-1] for i in s]
        s=" ".join(s)
        return s
