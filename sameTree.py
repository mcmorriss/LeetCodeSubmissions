# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [p]
        check = [q]
        while len(queue) > 0:
                x = queue.pop(0)
                y = check.pop(0)
                if x is None and y is None:
                    continue
                if x is None or y is None:
                    return False
                if x.val != y.val:
                    return False
                queue.append(x.left)
                queue.append(x.right)
                check.append(y.left)
                check.append(y.right)
        return True
