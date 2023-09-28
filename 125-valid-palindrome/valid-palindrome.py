class Solution:
    def isPalindrome(self, s: str) -> bool:
        # idea: time O(n), space O(1)
        # write a helper function to determine if it's alphanumeric character
        # in main function:
        # set 2 pointer from beg and end of string
        # check if 2 pointers equal, if no, return False, if yes, continue go inwards

        left, right = 0, len(s) - 1

        while left < right:
            # if not alphanumeric character, go inwards
            while left < right and not self.alphanum(s[left]):
                left += 1
            while left < right and not self.alphanum(s[right]):
                right -= 1
            # once both left and right are alphanumeric characters, check if the same
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
    
    def alphanum(self, c):
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )