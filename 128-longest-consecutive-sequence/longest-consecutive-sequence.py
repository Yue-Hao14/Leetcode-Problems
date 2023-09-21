class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # idea:
        # iterate through array and check if its -1 exists
            # if yes, it's not beginning of sequence, then move on; 
            # if no, this is begining of sequence
                # we then continue to check if its +1 exists, if yes then continue to check +2 etc. until it does not exist, count the length of sequence
                # check current sequence length vs. previous one
            # return max length

        # codes: time O(n), space O(n)
        # eliminate duplicates in the input array to increase time efficiency
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if it's the begining of a sequence
            if (n-1) not in numSet:
                length = 1
                while (n + length ) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        