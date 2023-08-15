class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # build a hash table to store nums[i] and its index i
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i

        # calculate complement = target - nums[i]
        # check to see if complement exist in hash table
            # if yes, return [i, numMap[complement]]
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return [] # no solution found

