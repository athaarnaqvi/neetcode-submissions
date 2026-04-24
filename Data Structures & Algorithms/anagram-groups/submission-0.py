class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results={}
        
        for word in strs:
            count=[0]*26

            for l in word:
                index = ord(l) - ord('a')
                count[index] += 1
            
            key =tuple(count)
            if key not in results:
                results[key] = []
            results[key].append(word)
        return list(results.values())

                