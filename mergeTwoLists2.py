# Date: September 27th, 2022

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        while p1:
            curr.next = p1
            p1 = p1.next
            curr = curr.next
        while p2:
            curr.next = p2
            p2 = p2.next
            curr = curr.next
        return head.next
      
      # Runtime: 40 ms, faster than 91.56% of Python3 online submissions for Merge Two Sorted Lists.
      # Memory Usage: 14 MB, less than 32.66% of Python3 online submissions for Merge Two Sorted Lists.
