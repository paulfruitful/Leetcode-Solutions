class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        compress=[]
        prev_char=chars[0]
        count=1
        for i in range(1,len(chars)):
            if chars[i]==prev_char:
                count+=1
            else:
                compress.append(prev_char)
                if count>1:
                 compress.extend(list(str(count)))
                prev_char=chars[i]
                count=1
        compress.append(prev_char)
        if count>1:
            compress.extend(list(str(count)))
        chars[:]=compress
        return len(chars)
        

