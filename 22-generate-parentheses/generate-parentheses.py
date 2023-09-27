class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # idea:
        # only add open parentheses if open < n
        # only add closing parenthese if close < open
        # valid result when open == close == n
        # do a recursion

        array = [] # store each parentheses in an array
        res = [] # store all outputs

        def backtrack(open_n, close_n):
            # base case
            if open_n == close_n == n:
                res.append("".join(array))
                return

            # add open parentheses
            if open_n < n:
                array.append("(")
                backtrack(open_n + 1, close_n)
                array.pop() 

            # add close parentheses
            if close_n < open_n:
                array.append(")")
                backtrack(open_n, close_n + 1)
                array.pop()
        
        backtrack(0,0)
        return res