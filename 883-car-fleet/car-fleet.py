class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # idea: O(n) time and space complexity
        # have an array with combined position and speed, like [(10,2),(8,4),(0,1),(5,1),(3,3)]
        # sort array by position in descending order (reverse)
        # go through array and push to stack
        # compare the [-1] and [-2] tuple in the stack to see if they crash by comparing time to destination
        # if yes, pop last one
        # if no, continue

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # sort it in descending order
        stack = []

        for p,s in pair:
            stack.append((target - p) / s) # time to destination
            # check if 2 car crash into each other
            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()

        return len(stack)