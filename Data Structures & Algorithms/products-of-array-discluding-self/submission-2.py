import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rets = [0] * len(nums)
        
        if len([n for n in nums if n==0])>=2:
            return rets

        if not 0 in nums:
            p = math.prod(nums)

            for i in range(len(nums)):
                rets[i] = int(p / nums[i])

        else:
            num_without_zero = [n for n in nums if n!=0] 
            p = math.prod(num_without_zero)
            
            for i in range(len(nums)):
                if nums[i] == 0:
                    rets[i] = p
                else:
                    nums[i] = 0

        return rets