class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # idea:
        # just copy num and then concatenate 2 of them

        # code:
        nums_2 = nums
        return nums + nums_2
        