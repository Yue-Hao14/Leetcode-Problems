class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # set 2 pointers (i and j) to iterate through the array
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i+1,len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    return [i,j]
