class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # idea:
        # we iterate from back and check the one num before target
        # if we can get to target from the one before, then move target 1 position to front
        # once target reach front, that means we can go from back to front, return true

        # code:
        # edge case: if array only has 1 num, then by default True
        if len(nums) == 1:
            return True

        target = len(nums) - 1 # last index in nums
        curr = len(nums) - 2 # 2nd to last index in nums

        # while curr > 0:
        # iterate backwards until i = 0
            # check if curr + nums[curr] which is furthest it can jump >= target
        for i in range(curr, -1, -1): 
            if curr + nums[curr] >= target:
                target = curr
            curr -= 1

        # once target is at index 0, means we can reach front from back, then True
        return target == 0

        