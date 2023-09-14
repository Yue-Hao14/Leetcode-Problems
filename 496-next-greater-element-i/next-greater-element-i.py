class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # stack method with time complexity O(n+m), space O(m)

        # idea:
        # Hashmap nums1 with key=index, value=num, so it's easy to find if num in nums2 exist in nums1 and its index
        # compare num in nums2 with a stack, if less than top of stack, add to it; if greater than top of stack, that means this num greater than anything in the stack, so find those smaller nums's index in nums1 and add current num to res


        # create a hashmap to num in nums1 as value and corresponding index as key
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        # create an array to store results with -1 default value
        res = [-1] * len(nums1)

        # create a stack to store nums in nums2
        stack = []
        # iterate through nums2
        for i in range(len(nums2)):
            current = nums2[i]
            # compare current vs. top of stack, if greater, find smaller nums' index, then add current to res at coresponding index
            while stack and current > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = current
            # add current to stack only if it exists in nums1
            if current in nums1Idx:
                stack.append(current)
                
        return res
