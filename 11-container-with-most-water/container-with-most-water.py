class Solution:
    def maxArea(self, height: List[int]) -> int:
        # idea: time O(n)
        # start left and right pointer from start and end of x axis, calculate area
        # move the pointer of smaller height inwards 

        # code:
        max_area = 0
        l, r = 0, len(height) - 1 # initiate at start and end of array

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            # shift smaller height pointer inwards, when equal shift either one
            if height[l] < height[r]:
                l += 1
            else :
                r -= 1
        
        return max_area
        