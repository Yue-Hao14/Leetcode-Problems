class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # idea:
        # iterate through the string and add count to hashmap
        # if len(hashmap.keys()) == 26, then True

        # code:
        hashmap = {}
        for letter in sentence:
            count = hashmap.get(letter,0) 
            count += 1
            hashmap[letter] = count

        return len(hashmap.keys()) == 26
            

        