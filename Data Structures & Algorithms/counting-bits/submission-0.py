class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n+1):
            nth = i.bit_count()
            bits.append(nth)
        return bits
            