class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache= [None]*201
        def solve(index, string):

            if index >= len(s):
                return True
            if string in wordDict:
                return True
            if cache[index] != None:
                return cache[index]

            for i in range(index, len(s)):
                temp = s[index:i+1]
                
                if temp in wordDict and solve(i+1, s):
                    cache[index] = True
                    return cache[index]
            cache[index] = False
            return cache[index]         
        

        ans = solve(0,s)
        return ans