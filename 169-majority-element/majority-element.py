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