class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # time complexity O(m*n), m is number of string in strs, n is average length of each string in strs

        # mapping charCount to list of Anagrams
        res = defaultdict(list) # make all values a list


        for str in strs:
            count = [0] * 26 # [0,0.....0] each 0 represents counts of a-z

            # iterate through the string to increment each letter in the count array
            for letter in str:
                count[ord(letter) - ord("a")] += 1 #increment count at the specific index corresponding to the letter, like letter "a" in char, increment count[0] by 1; letter "z" in char, then increment count[25] by 1
            
            # append current str to same charCount in the res hash map
            res[tuple(count)].append(str) # change count from list to tuple as list cannot be key for hash map in Python

        return res.values()


        
