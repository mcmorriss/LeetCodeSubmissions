# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        i = 0
        curr = head
        while True:
            if not curr:
                return None
            if curr not in nodes:
                nodes[curr] = i
                i += 1
                curr = curr.next
            else:
                return curr
