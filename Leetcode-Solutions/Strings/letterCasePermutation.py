class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(string,i,ret,s):
          if i==len(s):
              ret.append(string)
          else:
              if s[i].isalpha():
                  backtrack(string+s[i].swapcase(), i+1,ret,s)
              backtrack(string+s[i],i+1,ret,s)
        ret=[]
        backtrack("",0,ret,s)
        return ret
