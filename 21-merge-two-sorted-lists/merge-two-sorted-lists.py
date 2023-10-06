# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # idea:
        # iterate through the list with smaller head and check each node against list2
        # once one of the list is done, take the rest of the other list all together

        # code:
        # start with an empty LL first in case of edge case (2 empty input LL)
        dummy = ListNode()
        tail = dummy
        print(dummy)

        # check list1 vs. list2
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next # increment list1
            else:
                tail.next = list2
                list2 = list2.next # increment list2
            tail = tail.next # always increment tail
        
        # once one of list ends, put the rest of other list to tail LL one by one
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
        