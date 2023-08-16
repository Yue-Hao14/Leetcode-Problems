class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create 2 hash maps for each string to store the count of each letter
        # compare the 2 hash maps
        # if equal, return true; otherwise, false

        sCount, tCount = {}, {}

        for letter in s:
            sCount[letter] = sCount.get(letter,0) + 1
        
        for letter in t:
            tCount[letter] = tCount.get(letter,0) + 1
 
        if sCount == tCount:
            return True

        return False

