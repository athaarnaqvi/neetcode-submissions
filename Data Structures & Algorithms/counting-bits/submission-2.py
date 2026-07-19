class Solution:
    def countBits(self, n: int) -> List[int]:
        # built in approach
        # bits = []
        # for i in range(n+1):
        #     nth = i.bit_count()
        #     bits.append(nth)
        # return bits

        # dp approach
        bits = [1] * (n+1)
        if n == 0:
            return [0]
        bits[0] = 0
        for i in range(n+1):
            if i%2 != 0:
                bits[i] = bits[i//2] + 1
            else:
                bits[i] = bits[i//2] #// is used for integer division
        
        return bits


            