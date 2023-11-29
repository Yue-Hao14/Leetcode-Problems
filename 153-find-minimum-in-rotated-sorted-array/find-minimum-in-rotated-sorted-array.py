class Solution:
    def findMin(self, nums: List[int]) -> int:
        # idea:
        # do a binary search
        # if nums[left] > nums[right],
            # if nums[mid] > nums[left], move left
            # if nums[mid] < nums[right], move right
        # if nums[left] < nums[right], return left
        
        # code:
        left, right = 0, len(nums) - 1

        # when only 1 num in nums array
        if left == right:
            return nums[left]

        while left < right:
            mid = (left + right) // 2
            # when minimum element located at the last index
            if right - left == 1 and nums[right] < nums[left]:
                return nums[right]
            elif nums[left] > nums[right] and nums[mid] > nums[left]:
                left = mid
            elif nums[left] > nums[right] and nums[mid] < nums[left]:
                right = mid
            elif nums[left] < nums[right]:
                return nums[left]