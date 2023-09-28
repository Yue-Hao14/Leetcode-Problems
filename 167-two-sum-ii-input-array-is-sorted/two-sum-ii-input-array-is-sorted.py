class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # idea: O(n) time and space
        # build a hashmap with key of num and value of target - num
        # iterate through the array
        # look up its target-num in hashmap and check if it exists in array and its index

        # code: 
        hashmap = {}
        res = []

        # build hashmap
        for num in numbers:
            hashmap[num] = target - num
        
        # iterate through array
        for i, num in enumerate(numbers):
            diff = hashmap[num]
            if diff in numbers and diff != num:
                res.append(i + 1)
                res.append(numbers.index(diff) + 1)
                break
            if diff in numbers and diff == num:
                res.append(i + 1)
                res.append(numbers.index(diff) + 2)
                break
        
        return res
        