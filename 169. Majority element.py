# My solution using Hashmap/dict to count frequency with O(n) space
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create a hashmap/dict to store the frequency of each unique
        # element in the array
        frequencyMap = {}

        # loop through the array to count frequency of each unique element
        for num in nums:
            if frequencyMap.get(num) == None:
                frequencyMap[num] = 1
            else:
                frequencyMap[num] += 1

        # get the element with highest frequency
        majorityElement = max(frequencyMap, key=frequencyMap.get)

        return majorityElement


# Neetcode solution using HashMap with O(n) space
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > maxCount:
                maxCount = count[n]
                res = n
        return res

# Solution using Moore's voting algorithm with O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

            # count += (1 if n == res else -1)

        return candidate
