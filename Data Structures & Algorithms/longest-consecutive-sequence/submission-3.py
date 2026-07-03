class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(list(set(nums)))
        
        if len(nums) == 1:
            return 1

        gml = 0
        lml = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                lml+=1
            if nums[i] != nums[i-1] + 1 or i == len(nums) -1:
                print(lml)
                if gml < lml:
                    gml =lml
                lml = 1
        return gml


