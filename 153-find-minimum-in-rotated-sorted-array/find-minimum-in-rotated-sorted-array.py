class Solution:
    def findMin(self, nums: List[int]) -> int:
        # idea:
        # do a binary search
        # if nums[mid] >= nums[left], search right
        # else search left
        
        # code:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            # if nums already sorted correctly, nums[0] is the smallest
            if nums[left] < nums[right]:
                res = min(res, nums[left])

            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1
        
        return res
