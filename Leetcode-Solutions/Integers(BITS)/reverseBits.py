class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
     reversed_bits = 0
     for i in range(32):
        
        reversed_bits <<= 1

        if n & (1 << i):
            reversed_bits |= 1
    
     return reversed_bits
