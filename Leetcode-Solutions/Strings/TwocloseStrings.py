
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        
        char_freq1={}
        char_freq2={}

        for i in word1:
            char_freq1[i]=char_freq1.get(i,0)+1
        for i in word2:
            char_freq2[i]=char_freq2.get(i,0)+1
        return set(char_freq1)==set(char_freq2) and sorted(char_freq1.values())==sorted(char_freq2.values())
   
    
            
