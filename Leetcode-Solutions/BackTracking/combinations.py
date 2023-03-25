import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(start,current,k,result,n):
            if len(current)==k:
                result.append(current[:])
                return 
            for i in range(start,n+1):
                current.append(i)
                backtrack(i+1,current,k,result,n)
                current.pop()
        backtrack(1,[],k,result,n)
        return result
