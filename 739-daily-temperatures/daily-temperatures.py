class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # idea: use stack O(n) time and space
        # iterate through the array 
        # check if current temp > top of stack
            # if yes, pop top of stack and save index diff
            # if no, add current temp and its index to end of stack
        # default value 0

        # code:
        res = [0] * len(temperatures) # default value 0
        stack = [] # pair: [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append([temp, i])
        return res