class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # heat map to store count of each element
        count = {} 
        # nested list where index is the count/frequency, inner list holds element with the same frequency
        freq = [[] for i in range(len(nums) + 1)] 

        # count each element and store it in count heat map
        for n in nums:
            count[n] = 1 + count.get(n,0) 

        # extract element-count pair from hash map
        # append each element to coresponding count, same count element will be in the same index
        for element, count in count.items():
            freq[count].append(element)
        print(freq)

        # check from last index/highest frequency of the freq nested list 
        result = []
        for i in range(len(freq) - 1, 0, -1): # check from back to front
            # add inner list's element to result list until result list's length equal to k, then return result list
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result