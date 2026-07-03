class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        r1 = self.rob_without_circle(nums[:-1])
        r2 = self.rob_without_circle(nums[1:])
        return max(r1, r2)

    def rob_without_circle(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        r0 = 0
        r1 = 0
        for i in range(len(nums)):
            r2 = max(r1, r0 + nums[i])
            r0 = r1
            r1 = r2
        return r2
