class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea: binary search
        # we can first do binary search to locate which sub-array target may be in
        # then binary search within sub-array to find if target exists


        # code:
        # binary search to find the right sub array
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        while top <= bottom:
            middle_row = (top + bottom) // 2
            if target > matrix[middle_row][-1]:
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            else:
                break
        
        # if top and bottom out of space (cross), then we can never find target, then return False
        if not (top <= bottom):
            return False
        
        # binary search within sub array to see if target exists
        row = (top + bottom) // 2 # THE row that target may be in
        left, right = 0, cols - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        
        return False
        