class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        else:
            steps=0
            one,two=1,1
            for i in range(n-1):
                steps=one+two
                one=two
                two=steps
            return steps

        
