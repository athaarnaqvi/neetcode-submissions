class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1]*101
        n = len(s)
    
        
        def grouping(i,n):
            
            if (i==n):
                return 1
            if (i>=n):
                return 0
            if (s[i] == '0'):
                return 0
            if cache[i] != -1:
                return cache[i]
                  
            no_group = grouping(i+1,n)
            either_group = 0
            if (i+1 < n):
                if(s[i]=="1" or (s[i]=="2" and s[i+1]<="6")): 
                    either_group = grouping(i+2,n)

            cache[i] = either_group + no_group
            return cache[i]
        
        ways = grouping(0,n)

        return ways