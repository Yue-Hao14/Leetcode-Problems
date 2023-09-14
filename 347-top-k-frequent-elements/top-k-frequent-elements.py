class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # bucket sort method, time O(n), space O(n)

        # idea:
        # count frequency of each num and store in heatmap
        # put num to a nested frequency array, where index is the frequency of num, inner array holds all num with same frequency
        # itereate through nested frequency array from back until we get K elements

        # code:
        # create heat map to store count of each element, key = num, value = count of num in nums
        count = {} 
        # create nested list where index is the count/frequency, inner list holds element with the same frequency
        freq = [[] for i in range(len(nums) + 1)] 

        # count each element and store it in count heatmap
        for n in nums:
            count[n] = 1 + count.get(n,0) 

        # extract num-count pair from hash map
        # append each num to coresponding count, same count element will be in the same index
        for element, count in count.items():
            freq[count].append(element)
        print(freq)

        # check from last index/highest frequency of the freq nested list 
        result = []
        for i in range(len(freq) - 1, 0, -1): # check from back to front
            # add inner list's element to result list until result list's length equal to k, then return result list
            for n in freq[i]:
                result.append(n)
                # once len(result) reach k, return result
                if len(result) == k:
                    return result