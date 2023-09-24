class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # idea:
        # use stack because it always concerns last 2 numbers 
        # if num push to stack
        # if operator, take last 2 nums from stack, do operation, then push it to back of stack
        # repeat until only 1 num on stack

        # code: time and space O(n)
        stack = []

        for n in tokens:
            if n == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 + num2
                stack.append(num3)
            elif n == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num2 - num1
                stack.append(num3)
            elif n == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = num1 * num2
                stack.append(num3)
            elif n == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                num3 = int(num2 / num1) # int() will round towards 0
                stack.append(num3)
            else:
                stack.append(int(n))
        
        return stack[0]