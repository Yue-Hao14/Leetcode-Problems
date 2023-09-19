class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # ideas:
        # the key to decision is how much different is sending ith person to city A vs. city B, how big the difference is! 
        # So, we take the difference between 2 costs (c2-c1), if positive, means cost to B higher, go to A; if negative means cost to A higher, go to B
        # we sort the difference
        # first half go to B, second half go to A
        # add up costs
        
        
        # codes: time complexity O(nlogn)
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2-c1, c1, c2])
        diffs.sort() # it sort based on first 
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][2] # send to city B
            else:
                res += diffs[i][1] # send to city A
        return res