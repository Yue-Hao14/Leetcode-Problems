class RandomizedCollection:

    def __init__(self):
        # hashmap to store index(s) of each value
        self.hashmap = collections.defaultdict(set)
        # list to store each value
        self.list = []

    def insert(self, val: int) -> bool:
        self.hashmap[val].add(len(self.list))
        self.list.append(val)
        # when the len of self.hashmap[val] == 1, means first time seeing this element
        # otherwise, there are dups
        return len(self.hashmap[val]) == 1
        
    def remove(self, val: int) -> bool:
        if not self.hashmap[val]:
            return False
        else:
            last_element = self.list[-1]
            index = self.hashmap[val].pop()
            # replace the element with last element in list
            self.list[index] = last_element
            # add index to last_element's KVP in hashmap
            self.hashmap[last_element].add(index)
            # remove last index from the last element's KVP in hashmap
            self.hashmap[last_element].discard(len(self.list) - 1)
            # remove last element from the list
            self.list.pop()
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()