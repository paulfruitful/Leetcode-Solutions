class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        l=max(candies)

        for i in candies:
            maxer=max(i+extraCandies,l)
            result.append(maxer==(i+extraCandies))
        return result
