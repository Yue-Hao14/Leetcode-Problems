class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # idea: Two pointer method O(n) time, O(1) space
        # have left and right 2 pointers to start from beg and end of array
        # check if sum of 2 pointers larger than target, move right inward
        # if sum of 2 pointers smaller than target, move left inward
        # until sum of 2 pointers equal to target

        # code: 
        left, right = 0, len(numbers)-1

        
        # iterate through array
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]
        