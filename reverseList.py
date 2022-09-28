# Date: September 27th, 2022

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
      
      # Runtime: 39 ms, faster than 91.63% of Python3 online submissions for Reverse Linked List.
      # Memory Usage: 15.4 MB, less than 55.19% of Python3 online submissions for Reverse Linked List.
