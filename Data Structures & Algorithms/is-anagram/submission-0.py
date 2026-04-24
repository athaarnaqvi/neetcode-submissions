class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        
        for letter in t:
            if letter in s:
                s.remove(letter)
            else:
                return False
        
        return len(s) == 0