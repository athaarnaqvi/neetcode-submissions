class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
                count[n] = count.get(n,0)+1
            
        # top_k = sorted(count, key= count.get, reverse=True)[:k]
        #bucket sort

        buckets=[]
        for i in range(len(nums)+1):
            buckets.append([])
        
        for num in count:
            frequency=count[num]
            buckets[frequency].append(num)

        res=[]
        for freq in range(len(buckets)-1, 0,-1):
            for num in buckets[freq]:
                res.append(num)

                if len(res) == k :
                    return res

        # return top_k      