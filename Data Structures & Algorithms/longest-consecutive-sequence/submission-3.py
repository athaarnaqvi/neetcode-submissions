class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:   
            return 0
        maximum = max(nums)
        minimum = min(nums)
        
        count = {}

        for n in nums:
            count[n] = count.get(n,0)+1

        i = minimum

        total = 0 
        longest = 0
        while i>=minimum and i<=maximum:
            if i in count:
                total +=1               
                
            else:
                if longest < total:
                    longest = total

                total = 0
            i+=1
            
        longest = max(longest,total)  
        return longest