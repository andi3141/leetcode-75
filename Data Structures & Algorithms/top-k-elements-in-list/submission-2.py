class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)
        print(counts)
        
        if k >= len(counts):
            return list(counts.keys())
        
        c = sorted(counts.values(), reverse=True)
        print(c)
        t = c[k-1]
        print(t)
        res = []
        for (i,c) in counts.items():
            if c >=t:
                res.append(i)

        return res



