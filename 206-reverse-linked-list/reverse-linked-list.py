# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # idea: O(n) time but O(1) space
        # iterate through LL and store previous node in a variable, 
        # assign next to the previous node

        prev = None
        curr = head
     
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev
        