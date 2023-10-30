class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # idea:
        # iterate through string
        # push each string to an array until find a repeating characters, then count len(array) to update counter and clear arr

        # code:
        counter = 0
        arr = []

        for char in s:
            if char not in arr:
                arr.append(char)
                counter = max(counter, len(arr))
            else:
                counter = max(counter, len(arr))
                index = arr.index(char)
                arr = arr[index+1:]
                arr.append(char)
        
        return counter
        