class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)
        
        if k >= len(counts):
            return list(counts.keys())

        heap = []
        for (n, c) in counts.items():
            heapq.heappush(heap,(c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [l[1] for l in heap]