class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # idea:
        # only add open parentheses if open < n
        # only add closing parenthese if close < open
        # valid result when open == close == n
        # do a recursion

        res = [] # store all outputs

        def backtrack(open_n, close_n, path):
            # base case
            if open_n == close_n == n:
                res.append(path)
                return

            # add open parentheses
            if open_n < n:
                backtrack(open_n + 1, close_n, path + "(")

            # add close parentheses
            if close_n < open_n:
                backtrack(open_n, close_n + 1, path + ")")
        
        backtrack(0,0,"")
        return res