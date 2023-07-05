class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_stack=[]

        for i in s:
            if i !='*':
                result_stack.append(i)
            else:
                result_stack.pop()
        return ''.join(result_stack)
         



