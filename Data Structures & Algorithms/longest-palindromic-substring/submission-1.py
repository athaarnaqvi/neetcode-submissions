class Solution:
    def longestPalindrome(self, s: str) -> str:

        cache = [[False]*1001 for _ in range (1001)]
        def ispal(i,j):
            if(cache[i][j] != False):
                return cache[i][j]
            if (i>=j):
               
                return True
            elif(s[i] == s[j]):
                cache[i][j] = ispal(i+1,j-1)
                return cache[i][j]
            else:
                return False
        
        maxlen = 0
        sp = 0
        i=0
        while(i<len(s)):
            j=i
            while (j<len(s)):
                if ispal(i,j):
                    if j-i+1 > maxlen:
                        maxlen = j-i+1
                        sp = i
                j+=1
            i+=1
        
        
        substring = s[sp:sp+maxlen]

        return substring