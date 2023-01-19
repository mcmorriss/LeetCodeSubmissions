# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        curr = head

        while True:
            if curr.next:
                curr = curr.next
                i += 1
            else:
                break

        middle = i // 2

        while middle > 0:
            head = head.next
            middle -= 1
            
        return head
