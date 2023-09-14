class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # brute force method with time complexity O(n*m)and space complexity O(m)

        # create a hashmap to num in nums1 as value and corresponding index as key
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        # create an array to store results with -1 default value
        res = [-1] * len(nums1)

        # iterate through nums2
        for i in range(len(nums2)):
            current = nums2[i]
            # if current num in nums2 does not exist in nums1, skip
            if current not in nums1Idx:
                continue
            # find next greater element of current num in nums2    
            for j in range(i+1, len(nums2)):
                next = nums2[j]
                if next > current:
                    # find the index of same num in nums1
                    idx = nums1Idx[current]
                    # add next greater element to the right index in result array and stop this iteration
                    res[idx] = next
                    break
        return res