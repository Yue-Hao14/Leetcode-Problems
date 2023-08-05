class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # track current index and starts from 1 as the first element is always unique
        l = 1
        # iterate through the list and compare current element vs. the one before
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            else:
                r += 1

        return l
