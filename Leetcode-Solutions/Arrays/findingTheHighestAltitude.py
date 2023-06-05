class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest=0
        sum=0
        for i in gain:
            sum+=i
            highest=max(highest,sum)

        return highest
