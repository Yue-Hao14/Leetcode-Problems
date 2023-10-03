class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # idea: time and space O(n)
        # the height of possible rectangle are given, the key to this problem is to find out the length of rectangle which is finding begining and ending index
        # begining index starts at current index or the left most index where height < current height
        # ending index is when height < current height
        # so can use a stack to store [begining index, height]
        # iterate through height array, push current height to the stack if current height > top of stack, save current index (like height 5, 6)
        # pop each pair on the stack where height > current height and calculate that size based on height * (end - begin index) and compare if that's max size (pop height 5, 6 when curr height = 2)
        # then add current height, begin index = index of last poped height (curr height = 2, begin index = 2 where height 5 is)

        # code:
        max_area = 0
        stack = [] # pair: (beg index, height)

        for i, h in enumerate(heights):
            # set begining index to curr index first
            start = i
            # if curr height < top of stack, start poping stack until curr heigt >= top of stack
            while stack and stack[-1][1] > h:
                beg_index, height = stack.pop()
                max_area = max(max_area, height * (i - beg_index))
                # update begining index to left furthest index where height > curr height
                start = beg_index
            # push current stack once longer heights are all poped from stack
            stack.append((start, h))

        # once we iterate through heights array, need to calculate remaining possible rectangles left on stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area 

        