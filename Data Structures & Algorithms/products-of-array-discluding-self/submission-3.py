import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0] * len(nums)
        count_zeros = len([n for n in nums if n ==0])
        if count_zeros> 1:
            return output

        prod = np.prod([n for n in nums if n !=0])
        for i in range(len(nums)):
            if count_zeros==1:
                if nums[i]==0:
                    output[i]=prod
            else:
                output[i] = int(prod / nums[i])

        return output
