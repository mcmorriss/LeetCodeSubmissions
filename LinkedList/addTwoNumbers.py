# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        res = root
        carry = False
        while l1 and l2:
            temp_sum = 0
            temp_sum = l1.val + l2.val
            if carry:
                temp_sum += 1
                carry = False
            if temp_sum >= 10:
                temp_sum -= 10
                carry = True
            root.val = temp_sum
            if l1.next and l2.next:
                next_num = ListNode()
                root.next = next_num
                root = root.next
            elif l1.next or l2.next:
                next_num = ListNode()
                root.next = next_num
                root = root.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            temp_sum = l1.val
            if carry:
                temp_sum += 1
                carry = False
                if temp_sum == 10:
                    carry = True
                    temp_sum = 0
            root.val = temp_sum
            if l1.next:
                next_num = ListNode()
                root.next = next_num
                root = root.next
            l1 = l1.next
        while l2:
            temp_sum = l2.val
            if carry:
                temp_sum += 1
                carry = False
                if temp_sum == 10:
                    carry = True
                    temp_sum = 0
            root.val = temp_sum
            if l2.next:
                new_node = ListNode()
                root.next = new_node
                root = root.next
            l2 = l2.next
        if carry:
            root.next = ListNode(1)
        return res
