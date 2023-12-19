# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # idea:
        # go through the entire LL and find length
        # calculate mid
        # go to mid node

        # code:
        if not head.next: return head

        length = 0
        head_copy = head
        while head_copy:
            length += 1
            head_copy = head_copy.next

        mid = length // 2 + 1

        n = 1
        while n < mid:
            head = head.next
            n += 1

        return head
        