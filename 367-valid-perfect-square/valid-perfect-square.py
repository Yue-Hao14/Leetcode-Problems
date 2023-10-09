class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # idea: O(log n) time
        # use binary search
        # create an array with integers less than num
        # then binary search to see if middle ^2 == num

        # code:
        left, right = 1, num

        while left <= right:
            middle = (left + right) // 2
            if middle ** 2 < num:
                left = middle + 1
            elif middle ** 2 > num:
                right = middle - 1
            else:
                return True
        
        return False
        