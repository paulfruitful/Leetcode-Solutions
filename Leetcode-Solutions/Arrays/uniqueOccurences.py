class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic={}
        co=[]

        for i in arr:
          dic[i]=dic.get(i,0)+1
        for i in dic:
           co.append(dic[i])
        return len(co)==len(set(co))
       
            
    
