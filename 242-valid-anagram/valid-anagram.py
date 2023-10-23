class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # idea: time O(n) n = length of s or t; space O(n)
        # use a hashmap, key = letter, value = count of this letter
        # iterate through s and increment hashmap
        # iterate through t and decrement hashmap
        # if at the end, there is no value in hashmap > 0, then true

        # code:
        res = {}

        for letter in s:
            res[letter] = res.get(letter,0) + 1
        
        for letter in t:
            res[letter] = res.get(letter,0) - 1
        
        return set(res.values()) == {0} # convert value array to set so if all values in the list are 0, then it will be {0}

        