class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea:
        # iterate through array
        # check if curr num <= min(nums[i+1:])
            # if yes, move on
            # if no, find index of that min, swap

        
        # code:
        for i in range(len(nums)-1):
            num = nums[i]
            rest = nums[i+1:]
            smallest = min(rest)
            if num > smallest:
                # find index of the smallest in the rest of array
                smallest_index = rest.index(smallest) + i + 1 # rest array's index is shifted by i+1 compared to the original array
                # print(i, rest, smallest, smallest_index)
                nums[i] = nums[smallest_index]
                nums[smallest_index] = num
                # print(nums[i], nums[smallest_index])
            print(nums)
        return nums