class Solution:
    def isValid(self, s: str) -> bool:
        # idea:
        # use a hashmap to store parentheses pairs so later on we can check if its the right parentheses pair
        # use stack to check and store current parenthese vs. the one before
            # open parenthese, add to end of stack
            # close parenthese, check if same type vs. top of stack
                # if yes, pop prev from stack
                # if no, return False
        # if stack is not empty at the end, return False
        # if empty stack at the end, return True

        # code: time and space both O(n)
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            # if it's close parenthese
            if c in close_to_open:
                # check stack not empty and last one in stack match 
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            # if it's open parenthese
            else:
                stack.append(c)

        return True if not stack else False