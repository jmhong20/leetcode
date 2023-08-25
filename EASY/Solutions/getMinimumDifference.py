# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return

            vals.append(root.val)
            dfs(root.left)
            dfs(root.right)

        
        vals = []
        dfs(root)
        vals = sorted(vals, key = lambda x:x)
        min = float('inf')
        for i in range(len(vals) - 1):
            diff = abs(vals[i] - vals[i + 1])
            if diff < min:
                min = diff
        return min
