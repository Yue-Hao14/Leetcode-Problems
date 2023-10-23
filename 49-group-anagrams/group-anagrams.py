class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea: O(m*n) m = # of word in strs, n = avg length of each word
        # use a hashmap to store anagrams, key = letters in each word, value = anagrams in an array
        # for each word, we count what letter in it by building an array of 26 index with 0 value to start with
            # each index represent a letter, so index 0 is a
            # example: abc = [1,1,1,0,0,0......0]
        # words with same letters got stored together in the hashmap

        # code:
        res = defaultdict(list) # hashmap to store results

        for word in strs:
            count = [0] * 26 # a....z counter

            for letter in word:
                count[ord(letter) - ord("a")] += 1
            
            res[tuple(count)].append(word) # in python, array/list cannot be key so make it to a tuple
        
        return res.values()
        