class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        star_indices = []

        for i, char in enumerate(s):
          if char == "*":
            
            star_indices.append(i)
            continue
          result+=char
        for i in star_indices:
            




