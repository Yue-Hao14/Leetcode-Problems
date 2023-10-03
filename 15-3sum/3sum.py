class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # idea: time O(n^2) space O(1)
        # sort input array first, then use nested loop
        # iterate through nums
        # have an anchor pointer, left and right pointers where num[anchor] + num[left] + num[right] == 0
        # move left and right like 2 sum with sorted input array problem

        # code: 
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # skip iteration when num == nums before
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    # move left pointer further if current left same as the one before
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return res