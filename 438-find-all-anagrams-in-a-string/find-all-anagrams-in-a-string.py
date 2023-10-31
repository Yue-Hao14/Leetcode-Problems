class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # idea: sliding window O(n)
        # create p_count and s_count hashmap to store frequency:
            # key = letter, value = frequency/count
        # use l,r pointers to go through s
        # while move forward, remove old letter and add new letter to s_count 
        # if s_count == p_count, then anagram, add l pointer to res array

        # code
        # edge case
        if len(p) > len(s): return []

        p_count, s_count = {}, {}

        # compare first few letters in s
        for i in range(len(p)):
            # create p_count hashmap
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        res = [0] if s_count == p_count else []
        
        # compare rest of s
        l = 0
        for r in range(len(p), len(s)):
            # add r pointer letter to s_count
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            # decrement l pointer letter in s_count
            s_count[s[l]] -= 1

            # remove l pointer letter in s_count
            if s_count[s[l]] == 0:
                s_count.pop(s[l])

            # move l pointer forward
            l += 1

            # if s_count == p_count, anagram
            if s_count == p_count:
                res.append(l)

        return res