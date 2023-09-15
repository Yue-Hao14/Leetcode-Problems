class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time O(n), space O(1)

        # idea:
        # product of array except self = product of nums before (prefix) * product of nums after (postfix)
        # so we calculate prefix of each index and store in res array
        # then we take prefix * postfix of each index and overwrite in res array
        
        # code:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res