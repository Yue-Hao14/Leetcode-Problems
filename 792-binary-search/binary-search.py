class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # idea: time O(log n) space O(1)
        # binary search is finding middle point and compare it to target
        # then eliminate half and continue the search

        # code:

        # set left and right points to calculate middle pointer later
        left, right = 0, len(nums) - 1 

        while left <= right:
            middle = (left + right) // 2
            # if middle > target, eliminate first half and move left pointer
            # if middle < target, eliminate 2nd harf and move right pointer
            # if find it, return index
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1