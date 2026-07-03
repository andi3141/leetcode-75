class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]

        s = math.ceil(len(nums) / 2)
        h1 = nums[:s]
        h2 = nums[s:]
        print(h1)
        print(h2)
        # here
        if h1[-1] < h1[0]:
            m = self.findMin(h1)
        else:
            m = self.findMin(h2)
        

        return m