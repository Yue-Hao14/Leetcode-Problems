# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # idea: O(n) space and time
        # iterate through the list and store value of each node in a stack until get to the last node
        # once at last node, we start pop the stack to overwrite existing LL
        pointer = head
        stack = []
        
        # add val to stack
        while pointer:
            stack.append(pointer.val)
            pointer = pointer.next
        
        pointer = head # go back to head
        
        # overwrite current val by top of stack to reverse
        while pointer:
            pointer.val = stack.pop() 
            pointer = pointer.next
            
        return head
        