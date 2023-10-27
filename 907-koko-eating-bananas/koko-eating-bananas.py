class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # idea:
        # use binary search cuz 1 <= k <= max(piles)
        # then we can try k from this range 

        # code:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            middle = ( left + right ) // 2
            test_hour = 0
            for pile in piles:
                test_hour += math.ceil(pile / middle)
            
            # test_hour <= h, means we can try smaller k/middle
            if test_hour <= h:
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1
        
        return res
        