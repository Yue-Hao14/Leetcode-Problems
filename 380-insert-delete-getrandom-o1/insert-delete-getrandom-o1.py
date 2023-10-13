class RandomizedSet:
    # idea:
    # use an array to store value so can use random.choice O(1)
    # insert is easy O(1) using an array
    # for remove, if search array to get the index of element to be removed, already O(n)
        # only array.pop() is O(n) so I can replace the element with last element and then pop last one to achieve the result of removing THE element
        # then I need to a hashmap to store key = element's value, value = element's index in the array so i have easy access to each element's index and value

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        # remove KVP from hashmap while get the index of element
        removed_index = self.hashmap[val]
        last_element = self.array[-1]
        # replace removed element in array with the last element
        self.array[removed_index] = last_element
        # remove last_element from array
        self.array.pop()
        # update last_element's index in hashmap
        self.hashmap[last_element] = removed_index
        del self.hashmap[val]
        return True        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()