class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # set left and right pointers at begining and end of the string
        left, right = 0, len(s) - 1

        while left < right:
            # if left pointer is not an alphanumeric character, 
            # increment it to next character
            while left < right and not self.alphaNum(s[left]):
                left += 1
            # if right pointer is not an alphanumeric character, 
            # decrement it to previou character
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            # if left character != right character, not palindrome
            if s[left].lower() != s[right].lower():
                return False

            # increment/decrement left and right pointers to check next pair
            left += 1
            right -= 1
        # return True if all left == right
        return True
            

    def alphaNum(self, character):
        """
        check if character is an alphanumeric character
        """
        return (("a" <= character.lower() <= "z") 
        or ("0" <= character.lower() <= "9"))