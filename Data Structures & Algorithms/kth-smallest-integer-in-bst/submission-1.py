# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = None

        def dfs(node):
            

            if not node:
                return

            # visit left node
            dfs(node.left)
            
            # visit current node
            self.count = self.count +1
            if self.count == k:
                self.answer = node.val
                return
            
            # visit right node
            dfs(node.right)

        dfs(root)
        return self.answer
            
            
            