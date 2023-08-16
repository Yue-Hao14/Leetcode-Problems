class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create a hash map to store count of each num
        # whenever a value's count > 1, return true
        # otherwise return false
        countMap = {}

        for num in nums:
            if countMap.get(num) == None:
                countMap[num] = 1
            elif countMap[num] == 1:
                return True
        return False
