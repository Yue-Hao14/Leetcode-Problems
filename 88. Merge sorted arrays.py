# Approach : Two Pointer
# We can start with two pointers i and j, initialized to m-1 and n-1, respectively.
# We will also have another pointer k initialized to m+n-1, which will be used to
# keep track of the position in nums1 where we will be placing the larger element.
# Then we can start iterating from the end of the arrays i and j, and compare the
# elements at these positions. We will place the larger element in nums1 at position
# k, and decrement the corresponding pointer i or j accordingly. We will continue
# doing this until we have iterated through all the elements in nums2. If there are
# still elements left in nums1, we don't need to do anything because they are already
# in their correct place.


# Needcode solution with O(m+n) time complexity, O(1) space complexity
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index nums1
        last = m + n -1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n -1, last -1


# Leetcode best solution with O(m+n) time complexity, O(1) space complexity
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1 # pointer to nums1
        j = n - 1 # pointer to nums2
        k = m + n - 1 # pointer to track merged nums1 position

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1



# Approach : Using STL
# Traverse through nums2 and append its elements to the end of nums1 starting from index m.
# Sort the entire nums1 array using sort() function.

# Leetcode best solution with O((m+n)log(m+n)) time complexity, O(1) space complexity
class Solution:
    def merge(self, nums1, m, nums2, n):
      # add numbers in nums2 to the end of nums1
      for j in range(n):
          nums1[m+j] = nums2[j]
      # sort the entire nums1 array
      nums1.sort()
