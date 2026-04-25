class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for strings in strs:
            s+=str(len(strings))
            s+='#'
            s += strings
            
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        word = ""
        i=0
        while i < len(s):
            k = i
            while s[k] != '#':
                k+=1
            length = int(s[i:k])

            word = s[k+1:k+1+length]
            strs.append(word)

            i=k+1+length
            
            
               
        return strs 